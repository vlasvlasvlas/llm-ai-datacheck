# AI Document Analysis Script

## Overview

Within this repository, our mission is to automate the analysis of legal documents related to Artificial Intelligence (AI), adhering to a comprehensive definition of AI as outlined in our study. This definition broadens the scope, encompassing not only documents explicitly mentioning "Artificial Intelligence" but also those referencing related activities such as 'machine learning' or 'algorithmic modeling'. Our approach recognizes these AI-driven processes as valuable evidence, ensuring a thorough examination of frameworks and materials relevant to the expansive landscape of AI.

The repository leverages OpenAI's language model (replace with your preferred LLM name) to facilitate the extraction of insights and responses to specific queries embedded in legal documents. Our primary goal is to contribute substantively to the development of a global index of accountability in the dynamic field of AI. This initiative involves a meticulous analysis of thematic areas outlined in diverse legal documents, exploring the multifaceted dimensions of AI legislation and regulations.

Users engaging with this repository can explore its versatile functionalities, tailoring them to meet their specific requirements for legal document analysis. Whether scrutinizing frameworks, policies, or legislations, the repository provides a collaborative platform for extracting nuanced insights and fostering a deeper understanding of the legal landscape surrounding AI technologies.

To ensure transparency and accountability, users are encouraged to follow OpenAI's usage policies and guidelines when utilizing the resources within this repository. Additionally, we welcome ongoing contributions from the community, fostering a collective effort to enhance the repository's effectiveness and relevance in the ever-evolving landscape of AI legislation and accountability.


## Why? 

This repository serves a critical purpose in simplifying the daunting task of searching for specific thematic areas within extensive legal documents, particularly considering the global nature of AI-related legislations. By automating the analysis of diverse texts from various countries, the repository addresses the challenges associated with manually scouring through intricate legal frameworks. This initiative aims to streamline and expedite the identification of pertinent information related to Artificial Intelligence (AI), providing researchers and practitioners with a powerful tool to navigate and distill valuable insights from a wealth of legal documents.

The complexity of AI legislation, often dispersed across multilingual and nuanced texts, makes the manual search for thematic areas a time-consuming and challenging endeavor. This repository, powered by OpenAI's language model (replace with your preferred LLM name), significantly alleviates this burden by automating the extraction of relevant content. By doing so, it empowers users to efficiently pinpoint and comprehend specific legal aspects of AI, promoting a more accessible and accelerated understanding of global AI legislation.

In essence, the repository's overarching goal is to democratize access to crucial information embedded in legal texts, fostering a collaborative environment where researchers, policymakers, and enthusiasts can contribute to and benefit from a collective understanding of AI-related regulations on a global scale.

## AI Document Analysis

### Data (documents)

For a comprehensive analysis, this repository examines legal documents found in the `/data` directory. Users can choose any text files for analysis, and it's recommended to include the following metadata at the beginning of each document for better context:

```plaintext
COUNTRY_ISO: [Country Code]
COUNTRY_NAME: [Country Name]
COUNTRY_INSTITUTE: [Institute or Organization]
DOCUMENT_URL: [URL to Document]
---DOCUMENT_CONTENT_START---
[Document Content]
---DOCUMENT_CONTENT_END---
```


### Data Check - Thematic Areas

Thematic Areas within the `/datachecks` directory are Markdown files designed to guide the analysis and search for specific content within the legal documents located in the `/data` directory. These thematic areas provide a structured framework for understanding and categorizing information pertinent to the overarching goal of the repository. Each thematic area file may include the following sections:

#### Definitions:

This section outlines key terms and concepts relevant to the specific thematic area. It provides a clear understanding of the terminology used and establishes a foundation for interpreting information within the context of the defined themes.

#### Identification:

The Identification section delineates the criteria and indicators used to recognize and assess relevant content within legal documents. It guides users on how to identify specific elements or patterns that align with the thematic focus, ensuring a systematic and standardized approach to document analysis.

#### Considerations:

Considerations highlight additional factors or aspects that users should take into account when analyzing documents within the specified thematic area. These may include nuanced perspectives, potential challenges, or particular contexts that could influence the interpretation of information.

These thematic areas serve as invaluable tools for researchers and analysts, offering a structured methodology to streamline the analysis of legal documents related to Artificial Intelligence. By providing clear definitions, identification guidelines, and considerations, these files enhance the efficiency and accuracy of the document analysis process.


## Query Handling

The repo addresses queries specified in the `question` variable. Each response offers insights into how the document addresses AI-related thematic areas.

**Adaptability:** Feel free to explore and adapt the script to suit your specific requirements for AI document analysis.

**Assumption:** The script and this README assume a basic familiarity with Python and OpenAI's GPT models.

## How to Use

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

     ```plaintext
     API_KEY=your_openai_api_key
     ```

5. **Run the Script:**

   ```bash
   python analize.py
   ```

### Script Functionality

The script performs the following steps:

- Loads environment variables from a `.env` file.
- Configures the OpenAI API with the provided API key.
- Defines AI models and selects (replace with your preferred LLM name).
- Replaces special characters in the input text.
- Reads AI documents from the `data` folder.
- Reads markdown thematic area definitions from the `data` folder.
- Constructs prompts for AI based on document content.
- Utilizes OpenAI ChatCompletion to ask specific queries.
- Outputs and prints the responses.

## TO-DO's

- Include a troubleshooting section with common issues users might encounter and solutions.
- Highlight any security considerations or best practices, especially when dealing with sensitive AI documents.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
