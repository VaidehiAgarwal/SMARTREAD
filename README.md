### **SMARTREAD**
SMARTREAD is an AI-powered dashboard designed to assist users in extracting insightful information from uploaded datasets or connected Google Sheets. Leveraging APIs like SerpAPI for web search and OpenAI for natural language processing, SMARTREAD simplifies the process of gathering and structuring information dynamically based on user queries.

---

## **Features**
1. **File Upload and Google Sheets Integration**:
   - Upload CSV files or connect Google Sheets for data input.
   - Preview and select the main column to be processed.
2. **Custom Query Inputs**:
   - Define the type of information to retrieve using intuitive prompts.
   - Support for multiple information types, including *Mission*, *Products*, *Jobs*, and more.
3. **Web Search and Processing**:
   - Perform automated web searches for selected entities using APIs.
   - Extract relevant snippets from web results dynamically.
4. **LLM Integration**:
   - Summarize and structure the information using OpenAI's GPT model.
5. **Results Display and Download**:
   - View structured results in a user-friendly table format.
   - Download results as a CSV file.

---

## **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/smartread-ai-agent.git
   cd smartread-ai-agent
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   - Create a `.env` file in the root directory and add the following keys:
     ```
     SERPAPI_KEY=<your-serpapi-key>
     OPENAI_API_KEY=<your-openai-key>
     GOOGLE_SHEETS_CREDENTIALS_PATH=<path-to-your-google-credentials.json>
     ```

4. **Run the Application**:
   ```bash
   streamlit run fn.py
   ```

---

## **Usage Guide**
1. Launch the app using the command above.
2. Use the **Upload CSV** option to upload your dataset or connect to a Google Sheet by providing its ID.
3. Select the column containing entities for which you want to retrieve information.
4. Choose the type of information to search for (e.g., *News*, *Ratings*, etc.).
5. Click **Start SMART Search** to retrieve and view the results.
6. Download the extracted results as a CSV.

---

## **APIs and Tools**
- **SerpAPI**: For web search and result retrieval.
- **OpenAI GPT**: For summarizing and structuring the extracted information.
- **Google Sheets API**: For real-time integration with Google Sheets.
- **Streamlit**: For building the interactive user interface.

---

## **Project Structure**
```
smartread-ai-agent/
│
├── fn.py                     # Main application script
├── requirements.txt          # Dependencies for the project
├── .env                      # Environment variables (not included in the repo)
├── credentials.json          # Google Sheets API credentials (not included in the repo)
├── README.md                 # Project documentation
└── outputs/                  # Directory for downloaded files
```

---

## **Demo**
Check out the project in action through this [Loom Video Walkthrough](https://drive.google.com/file/d/1sf6jC8NgddOjCcYktueQGszE-x8Qm7sG/view?usp=drive_link)


---

## **License**
This project does not include a license. By default, **all rights are reserved**, and permission is required to use, modify, or distribute the software. If you would like to use this project, please contact the author.

---
