import os
from dotenv import load_dotenv
import openai
import PyPDF2
import sys
import pandas as pd
import numpy as np
from io import StringIO


# Load environment variables from the .env file
# Reload the variables in your '.env' file (override the existing variables)
load_dotenv(".env", override=True)

# Now you can access environment variables using the `os.getenv()` function
api_key = os.getenv("API_KEY")
print("api_key:", api_key)

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
        "`": "",
        "|No|": '|"No"|',
        "|Yes|": '|"Yes"|',
    }

    for original, replacement in replacements.items():
        text = text.replace(original, replacement)

    return text


def replace_line_breaks(text, replacement=" "):
    """
    Replace all types of line breaks in the input text with the specified replacement.

    Parameters:
    - text (str): The input text with line breaks.
    - replacement (str): The string to replace line breaks with. Default is a space.

    Returns:
    - str: The modified text with line breaks replaced.
    """
    return (
        text.replace("\n", replacement)
        .replace("\r\n", replacement)
        .replace("\r", replacement)
    )


# List of files in the 'data' folder
data_files = os.listdir("data")

# data_files_prefix is a list of prefixes to filter the files in the 'data' folder
data_files_prefix = ["EU_"]

# data_files_postfix is a list of postfixes to filter the files in the 'data' folder
data_files_postfix = [".txt"]

# Filter only text files with the prefix in data_files_prefix and ending with .txt
data_files = [
    file
    for file in data_files
    if any(file.endswith(ext) for ext in data_files_postfix)
    and any(file.startswith(prefix) for prefix in data_files_prefix)
]
print("data_files:", data_files)

# data_checks is a list of files in the 'datachecks' folder
data_checks = os.listdir("datachecks")

# data_checks_postfix is a list of postfixes to filter the files in the 'datachecks' folder
data_checks_postfix = [".md"]

data_checks = [
    file
    for file in data_checks
    if any(file.endswith(ext) for ext in data_checks_postfix)
]
print("data_checks:", data_checks)

# AI definition for analysis
ai_definition = "For purposes of this study, evidence relating to AI will be understood in a broad sense. For example, when researchers are requested to analyze frameworks related to AI, accepted evidence will be those frameworks that use language referring to ‘Artificial Intelligence’ to define their object, or those that cover activities fitting in the above-mentioned definition, regardless of whether the specific term ‘Artificial Intelligence’ has been used. For example, if there is mention of ‘machine learning’ or ‘algorithmic modeling’ but no mention of ‘artificial intelligence’ in a document, please consider these as evidence relating to AI since they mention AI-driven processes"

# Question prompt for AI
question = """
Kindly provide clear and concise responses to the following queries.
Output Format: CSV Pipe separated UTF-8 with the following columns HEADER: answer_1_fullanswer | answer_2_yesno | answer_2_fullanswer | answer_3_yesno | answer_3_fullanswer | answer_4_yesno | answer_4_fullanswer | answer_5_doc_date 
- ALWAYS include the column names in the first row of the CSV file.
- ALWAYS USE pipe (|) as the separator AND double quote delimiter (") for data.
- Yes/No answers (columns that ends with _yesno) must be answered with a Yes or No.
- Full answers (columns that ends with _fullanswer) must not be cutted or truncated ensuring that these columnbased answers are complete and full extense.
- Must return 1 row per document analyzed.

Please respond in fluent English and initiate your responses with a definitive answer for each specific question:

1) Identify the thematic area outlined in the markdown guide for analysis.

2) Determine with utmost clarity whether the document precisely addresses the topic of artificial intelligence in a specific and unambiguous manner, referencing the provided definition: {ai_definition}.

3) Conclusively establish if the document specifically addresses the identified thematic area.  Always provide a detailed explanation of how the document specifically addresses the indicated thematic area outlined in the markdown rule guide.

4) Provide a detailed explanation of how the document addresses the specified thematic area outlined in the markdown rule guide. Ensure your response includes specific references to the relevant chapter and article of the document.

5) Find the release date or last update date of the document.

Responses should be expressed in a extense professional, precise, and neutral manner, with a particular emphasis on clarity to ensure the highest reliability and quality in your answers.

""".format(
    ai_definition=ai_definition
)

# prompt to fix and repair a csv data file text
refining_output = """
You are the best data analyzer and CSV fixer.
gold rules:
- You must fix the content that is given to you, its suposed to be a CSV with 1 header and 1 row.
- Output Format needed: CSV Pipe separated UTF-8 with the following columns HEADER: answer_1_fullanswer | answer_2_yesno | answer_2_fullanswer | answer_3_yesno | answer_3_fullanswer | answer_4_yesno | answer_4_fullanswer | answer_5_doc_date 
- for answer_5_doc-date you must find and fix the date: it must be in the following format: YYYY-MM-DD
- IF columns exists and are correct, you must not change them.
- ALWAYS remove linebreaks from inside each column.
- ALWAYS include the column names in the first row of the CSV file.
- ALWAYS USE pipe (|) as the separator AND double quote delimiter (") for data.
- NEVER change the meaning of the text given to you, you must only fix the CSV format!.
- ALWAYS check expected fields. they MUST be 8. If they are more, PLEASE CHECK POSSIBLE LINE BREAKS INSIDE THE TEXT OF EACH COLUMN AND REMOVE THEM.
As output I only need the header and the row, you must not add anything to the response. Give your best!
""".format()

refining_answer = "please fix the input and prepare it as the CSV i need based on the rules i gave you"


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
        "answer_5_doc_date",
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

        print("-------------------------------")
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
        print("-> response:", response)

        print("-----> fixing question!")
        response_fixed = ask_question(refining_output, response, refining_answer)
        response_fixed = replace_special_characters(response_fixed)

        # Fix special chars and rearrange pipes and double quotes
        response_fixed = response_fixed.replace('"', "").replace("|", '"|"')
        response_fixed = "\n".join(
            f'"{line.strip()}"' for line in response_fixed.split("\n")
        )
        print("-> response_fixed:", response_fixed)

        # Create a DataFrame from the CSV-formatted response, with comma as separator and double quotees for data
        df_response = pd.read_csv(StringIO(response_fixed), sep="|")

        # remove empty rows from df_response
        df_response = df_response.dropna(how="all")

        # Add additional columns
        df_response["data_file"] = replace_line_breaks(
            replace_special_characters(data_file).replace('"', "").replace("|", "")
        )
        df_response["data_check_file"] = replace_line_breaks(
            replace_special_characters(data_check_file)
            .replace('"', "")
            .replace("|", "")
        )
        df_response["prompt"] = replace_line_breaks(
            replace_special_characters(bible_prompt).replace('"', "").replace("|", "")
        )
        df_response["ai_model"] = replace_line_breaks(
            replace_special_characters(ai_model).replace('"', "").replace("|", "")
        )
        df_response["date"] = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")

        # fill df_master with df_response as one row
        df_master = pd.concat([df_master, df_response], axis=0, ignore_index=True)
        print("\n--> df master updated:")
        print(df_master)


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
