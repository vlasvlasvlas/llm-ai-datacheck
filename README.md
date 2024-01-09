# AI Document Analysis Script

## Why?

This Python script is designed to analyze legal documents related to Artificial Intelligence (AI). It utilizes a language model (replace with your preferred LLM name) to extract insights and responses to specific queries. The purpose of this script is to aid in the development of a global index of accountability in AI by examining thematic areas outlined in legal documents.


## Legal Document Analysis

The legal documents analyzed include:

- **Your_Selected_Document.txt**

The script is tailored to address queries outlined in the variable `pregunta`. Each response provides insights into the document's treatment of AI-related thematic areas.

**Important:** 

Ensure you comply with OpenAI's usage policies and guidelines when running the script.

Feel free to explore and adapt the script for your specific legal document analysis needs.

*Note: The script and this README assume familiarity with Python and OpenAI's GPT models.*


## How?

### Installation Instructions

1. **Clone the Repository:**

```bash
   git clone <repository_url>
   cd <repository_name>
```

2. **Create a Virtual Environment (Optional but Recommended):**

```bash
python -m venv venv   
source venv/bin/activate  

# On Windows, use `venv\\Scripts\\activate`
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables:**

- Create a `.env` file in the root of the project.
- Add your OpenAI API key to the `.env` file:

```API_KEY=your_openai_api_key```

5. **Run the Script:**

```bash
python script.py
```
### Script Functionality

The script performs the following steps:

- Loads environment variables from a `.env` file.
- Configures the OpenAI API with the provided API key.
- Defines AI models and selects (replace with your preferred LLM name).
- Replaces special characters in the input text.
- Reads legal documents from the `data` folder.
- Constructs prompts for AI based on document content.
- Utilizes OpenAI ChatCompletion to ask specific queries.
- Outputs and prints the responses.
