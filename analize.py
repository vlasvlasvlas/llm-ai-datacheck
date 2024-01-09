import os
from dotenv import load_dotenv
import openai
import PyPDF2
import sys 

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno usando la función `os.getenv()`
api_key = os.getenv("API_KEY")

# Configurar OpenAI
openai.api_key = api_key

ai_models = ['gpt-3.5-turbo-1106', 'gpt-4-1106-preview']
ai_model = ai_models[1]
print("ai_model:",ai_model)


# replace func
def replace_special_characters(text):
    replacements = {
        "“": "\"",
        "”": "\"",
        "–": "-",
        "—": "--",
        "‘": "'",
        "’": "'"
    }

    for original, replacement in replacements.items():
        text = text.replace(original, replacement)

    return text




# abrir doc ley
file = "FRAMEWORKACTONINTELLIGENTINFORMATIZATION" #"MEN-2023-7-APN-PTE_Proyecto_de_Ley_que"
with open('data/'+file+".txt", 'r', encoding='utf-8') as f:
    texto = f.read()

# fix special chars
texto = replace_special_characters(texto)

# bibles
bibles = ['1.1.1.national_ai_policy.md','1.1.2.impact_assessments.md']

# ai definition
ai_definition = "For purposes of this study, evidence relating to AI will be understood in a broad sense. For example when researchers are requested to analyse frameworks related to AI, evidence accepted will be those frameworks that use language that refer to ‘Artificial Intelligence’ to define their object, or those that cover activities that fit in the above mentioned definition, regardless of whether the specific term ‘Artificial Intelligence’ has been used. For example, if there is mention of ‘machine learning’ or ‘algorithmic modelling’ but no mention of ‘artificial intelligence’ in a document, please consider these as evidence relating to AI since they mention AI-driven processes"

# pregunta
pregunta = """
Kindly provide clear and concise responses to the following queries (please respond in fluent English and initiate your responses with a definitive answer for each specific question):

1) Identify the thematic area outlined in the markdown guide for analysis.

2) Determine with utmost clarity whether the document precisely addresses the topic of artificial intelligence in a specific and unambiguous manner, referencing the provided definition: {ai_definition}.

3) Conclusively establish if the document specifically addresses the identified thematic area.  Always provide a detailed explanation of how the document specifically addresses the indicated thematic area outlined in the markdown rule guide.

4) Provide a detailed explanation of how the document addresses the specified thematic area outlined in the markdown rule guide. Ensure your response includes specific references to the relevant chapter and article of the document.

Responses should be expressed in a professional, precise, and neutral manner, with a particular emphasis on clarity to ensure the highest reliability in your answers.
""".format(ai_definition=ai_definition)


def hacer_pregunta(texto, pregunta):

    print("asking question..")

    respuesta = openai.ChatCompletion.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": bible_prompt},
            {"role": "user", "content": texto},
            {"role": "user", "content": pregunta},
        ],
    )
    
    return respuesta["choices"][0]["message"]["content"].strip()



# Crear o abrir el archivo de salida
#with open('answers.txt', 'a', encoding='utf-8') as file:

for bible in bibles:

    with open('data/'+bible, 'r', encoding='utf-8') as f:
        bibletxt = f.read()

    # bible prompt
    bible_prompt = """
    You are working on the development of a global index of accountability in artificial intelligence. Specifically, you are analyzing specific thematic areas. Your approach must be highly serious and precise. If there is something you do not know or are not entirely clear about, you must explicitly state that you do not know. Your perspective on the topic should remain neutral. Whenever possible, provide a comprehensive context for your response. You are required to respond in Spanish with an IQ of at least 150. The following Markdown format will guide you in understanding what the thematic area entails and provide tools to identify elements of the thematic area in any document.
    -- BEGIN MARKDOWN RULES GUIDE -- {bibletxt} -- END MARKDOWN RULES GUIDE --
    """.format(bibletxt=bibletxt)


    # texto
    texto = """
    -- BEGIN LEGAL DOCUMENT --
    {texto}
    -- END LEGAL DOCUMENT --
    """.format(texto=texto)




    respuesta = hacer_pregunta(texto, pregunta)

    print("--------------------")
    print("Question: ", pregunta)
    print("--------------------")
    print("Answer: ", respuesta)

    #file.write("Question: " + pregunta + "\n")
    #file.write("Answer: " + respuesta + "\n")