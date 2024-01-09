import os
from dotenv import load_dotenv
import openai
import PyPDF2
import sys
import pandas as pd
import numpy as np
from io import StringIO


# Load environment variables from the .env file
load_dotenv()

# Now you can access environment variables using the `os.getenv()` function
api_key = os.getenv("API_KEY")

# Configure OpenAI
openai.api_key = api_key

# List of AI models
ai_models = ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"]
# Select AI model
ai_model = ai_models[1]
print("ai_model:", ai_model)


# Function to replace special characters in text
def replace_special_characters(text):
    replacements = {
        "“": "",
        "”": "",
        "–": "-",
        "—": "--",
        "‘": "'",
        "’": "'",
        "```csv": "",
        "`": ""
    }

    for original, replacement in replacements.items():
        text = text.replace(original, replacement)

    return text


# List of files in the 'data' folder
data_files = os.listdir("data")
data_checks = os.listdir("datachecks")

# Filter only text files
data_files = [file for file in data_files if file.endswith(".txt")]  # as textfiles
print("data_files:", data_files)

data_checks = [file for file in data_checks if file.endswith(".md")]  # as markdown
print("data_checks:", data_checks)


# AI definition for analysis
ai_definition = "For purposes of this study, evidence relating to AI will be understood in a broad sense. For example, when researchers are requested to analyze frameworks related to AI, accepted evidence will be those frameworks that use language referring to ‘Artificial Intelligence’ to define their object, or those that cover activities fitting in the above-mentioned definition, regardless of whether the specific term ‘Artificial Intelligence’ has been used. For example, if there is mention of ‘machine learning’ or ‘algorithmic modeling’ but no mention of ‘artificial intelligence’ in a document, please consider these as evidence relating to AI since they mention AI-driven processes"

# Question prompt for AI
question = """
Kindly provide clear and concise responses to the following queries.
Output Format: CSV Pipe separated UTF-8 with the following columns: answer_1_fullanswer | answer_2_yesno | answer_2_fullanswer | answer_3_yesno | answer_3_fullanswer | answer_4_yesno | answer_4_fullanswer
- Dont forget: include the column names in the first row of the CSV file, use pipe separation (|) and always use quotes to enclose the answers. 
- Yes/No answers (columns that ends with _yesno) must be answered with a Yes or No.
- Full answers (columns that ends with _fullanswer) must not be cutted or truncated ensuring that these columnbased answers are complete and full extense.
- Must return 1 row per document analyzed.

Please respond in fluent English and initiate your responses with a definitive answer for each specific question:

1) Identify the thematic area outlined in the markdown guide for analysis.

2) Determine with utmost clarity whether the document precisely addresses the topic of artificial intelligence in a specific and unambiguous manner, referencing the provided definition: {ai_definition}.

3) Conclusively establish if the document specifically addresses the identified thematic area.  Always provide a detailed explanation of how the document specifically addresses the indicated thematic area outlined in the markdown rule guide.

4) Provide a detailed explanation of how the document addresses the specified thematic area outlined in the markdown rule guide. Ensure your response includes specific references to the relevant chapter and article of the document.

Responses should be expressed in a extense professional, precise, and neutral manner, with a particular emphasis on clarity to ensure the highest reliability and quality in your answers.

""".format(
    ai_definition=ai_definition
)


# Function to ask questions using OpenAI's ChatCompletion
def ask_question(bible_prompt, text, question):
    print("asking question..")

    response = openai.ChatCompletion.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": bible_prompt},
            {"role": "user", "content": text},
            {"role": "user", "content": question},
        ],
    )

    return response["choices"][0]["message"]["content"].strip()


# create empty master dataframe
df_master = pd.DataFrame(
    columns=[
        "answer_1_fullanswer",
        "answer_2_yesno",
        "answer_2_fullanswer",
        "answer_3_yesno",
        "answer_3_fullanswer",
        "answer_4_yesno",
        "answer_4_fullanswer",
        "data_file",
        "data_check_file",
        "prompt",
        "ai_model",
        "date",
    ]
)

# Iterate over data_file in the 'data' folder
for data_file in data_files:
    print("analyzing file:", data_file)

    # Read text from data_file
    with open("data/" + data_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Fix special chars
    text = replace_special_characters(text)

    # get text from file in data_checks variable that includes list of files where i must extract the text
    for data_check_file in data_checks:
        with open("datachecks/" + data_check_file, "r", encoding="utf-8") as f:
            textcheck = f.read()

        print("checking file:", data_check_file)

        # Fix special chars
        text = replace_special_characters(text)

        # Bible prompt
        bible_prompt = """
        You are working on the development of a global index of accountability in artificial intelligence. Specifically, you are analyzing specific thematic areas. Your approach must be highly serious and precise. If there is something you do not know or are not entirely clear about, you must explicitly state that you do not know. Your perspective on the topic should remain neutral. Whenever possible, provide a comprehensive context for your response. You are required to respond with an IQ of at least 150. The following Markdown format will guide you in understanding what the thematic area entails and provide tools to identify elements of the thematic area in any document.
        -- BEGIN MARKDOWN RULES GUIDE -- {textcheck} -- END MARKDOWN RULES GUIDE --
        """.format(
            textcheck=textcheck
        )

        # Text
        text = """
        -- BEGIN AI RELATED LEGAL DOCUMENT --
        {text}
        -- END AI RELATED LEGAL DOCUMENT --
        """.format(
            text=text
        )

        # Ask question
        response = ask_question(bible_prompt, text, question)

        # Fix special chars
        response = replace_special_characters(response)

        print("response:", response)
        
        # Create a DataFrame from the CSV-formatted response, with comma as separator and double quotees for data
        df_response = pd.read_csv(StringIO(response), sep="|", quotechar='"')
        # check dataframe

        # remove empty rows from df_response
        df_response = df_response.dropna(how="all")

        # Add additional columns
        df_response["data_file"] = replace_special_characters(data_file).replace('"', '')
        df_response["data_check_file"] = replace_special_characters(data_check_file).replace('"', '')
        df_response["prompt"] = replace_special_characters(bible_prompt).replace('"', '')
        df_response["ai_model"] = replace_special_characters(ai_model).replace('"', '')
        df_response["date"] = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")

        # fill df_master with df_response as one row
        df_master = pd.concat([df_master, df_response], axis=0, ignore_index=True)

# remove empty rows from df_master
df_master = df_master.dropna(how="all")

# Save df_master as CSV in dataoutputs/ folder as output + timestamp as yyyy-mm-dd-hh-ss + .csv
df_master.to_csv(
    "dataoutputs/output-"
    + pd.to_datetime("today").strftime("%Y-%m-%d-%H-%M-%S")
    + ".csv",
    index=False,
)

# show df_master results
print("df_master:", df_master)
print("done!")
