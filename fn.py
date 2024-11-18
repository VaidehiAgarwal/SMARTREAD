import streamlit as st
import pandas as pd
import requests
import openai
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="SMARTREAD", page_icon="📘", layout="wide")

SERPAPI_KEY = "your-serpapi-key" #enter your key
OPENAI_API_KEY = "your-openaiapi-key" #enter your key
openai.api_key = OPENAI_API_KEY

st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #6E7C92, #A29BB7, #54687A);
            background-size: 300% 300%;
            animation: GradientShift 6s ease infinite;
        }
        @keyframes GradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        h1 {
            color: #1E3A8A;
            text-align: center;
        }
        h2, h3, h4 {
            color: #4B5563;
        }
    </style>
""", unsafe_allow_html=True)

def authenticate_google_sheets():
    creds = Credentials.from_service_account_file(
        'path-of.json', 
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    ) #enter the path
    service = build('sheets', 'v4', credentials=creds)
    return service

def fetch_google_sheets_data(sheet_id, range_name):
    service = authenticate_google_sheets()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return result.get('values', [])

def search_web(query, api_key):
    try:
        url = f"https://serpapi.com/search.json?q={query}&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('organic_results', [])
    except requests.exceptions.RequestException:
        return []

def extract_info_from_results(search_results):
    if not search_results:
        return "No information found"
    return [result.get('snippet', 'No snippet available') for result in search_results[:3]]

def generate_summary(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following information concisely:\n{text}",
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception:
        return "None"

st.sidebar.header("Read SMART with SMARTREAD!")
uploaded_file = st.sidebar.file_uploader("Drop your CSV here!", type="csv")
sheet_id = st.sidebar.text_input("Got Google Sheets? Enter its ID!")
range_name = st.sidebar.text_input("Specify the range (e.g., A1:A10)")

st.markdown("# SMARTREAD")
st.markdown("### Explore Beyond the Basics: Be Quick, Smart and Insightful!")

st.markdown("""
1. **Upload your data**: Either via CSV or Google Sheets.
2. **Select your options**: Choose the column and the types of information to search for.
3. **Let SMARTREAD do the work**: Extract and summarize insightful information.
""")

data = None
if uploaded_file:
    data = pd.read_csv(uploaded_file)
elif sheet_id and range_name:
    data = pd.DataFrame(fetch_google_sheets_data(sheet_id, range_name))

if data is not None:
    st.markdown("### Here’s Your Data:")
    st.dataframe(data.head(), use_container_width=True)

    entity_column = st.sidebar.selectbox("Which column holds the entities?", data.columns)
    search_types = st.sidebar.multiselect("What information do you want to search for?", [
        "Mission", "Products", "Research Papers", "Team Members", "Contact Info", 
        "News", "Details", "Jobs", "Ratings", "Reviews"
    ])

    if st.sidebar.button("Start SMART Search"):
        st.markdown("### Results:")
        results = []
        progress_bar = st.progress(0)
        total_entities = len(data[entity_column].dropna())
        
        for idx, entity in enumerate(data[entity_column].dropna(), 1):
            progress_bar.progress(idx / total_entities)
            result_entry = {"Entity": entity}
            
            for search_type in search_types:
                query = f"{search_type} about {entity}"
                search_results = search_web(query, SERPAPI_KEY)
                snippets = extract_info_from_results(search_results)
                result_entry[search_type] = " ".join(snippets)
            
            results.append(result_entry)

        progress_bar.empty()
        results_df = pd.DataFrame(results)
        st.dataframe(results_df, use_container_width=True)
        st.download_button(
            label="Download Results",
            data=results_df.to_csv(index=False),
            file_name="SMARTREAD_results.csv",
            mime="text/csv"
        )
else:
    st.warning("Upload a file or enter Google Sheets details to proceed.")
