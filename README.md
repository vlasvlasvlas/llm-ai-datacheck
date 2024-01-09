# AI Document Analysis Script

# AI Legal Document Analysis

Automate the analysis of AI-related legal documents with this repository. Explore diverse thematic areas within the expansive field of Artificial Intelligence (AI) legislation, including related terms like 'machine learning' or 'algorithmic modeling.' Leveraging language models, the repository extracts insights, aiming to contribute to a global index of AI accountability.

Customize the analysis for AI-related legal documents, allowing users to focus on multiple user-defined thematic areas with flexibility.

Explore, analyze, and advance accountability in the dynamic landscape of AI-related legalities.


## Why? 

This repository simplifies the search for specific thematic areas in extensive AI-related legal documents, addressing challenges associated with manually exploring complex global legal frameworks. By automating the analysis of diverse texts from different countries, the tool streamlines the identification of relevant information in the field of AI, providing researchers and professionals with a powerful tool to extract valuable insights from a wide range of legal documents.

The complexity of AI legislation, dispersed in multilingual and nuanced texts, makes the manual search for thematic areas time-consuming and challenging. This repository, powered by language models, significantly alleviates this burden by automating the extraction of relevant content. It empowers users to efficiently identify and comprehend specific aspects of AI legislation, promoting a more accessible and accelerated understanding of global AI regulations.

In essence, the repository's primary goal is to democratize access to crucial information in AI-related legal texts, fostering a collaborative environment where researchers, policymakers, and enthusiasts can contribute to and benefit from a collective understanding of global AI regulations.

## Document Analysis

### Data (ai related documents)

For a comprehensive analysis, this repository examines AI related legal documents found in the `/data` directory. Users can choose any text files for analysis, and it's recommended to include the following metadata at the beginning of each document for better context:

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

Thematic Areas within the `/datachecks` directory are Markdown files designed to guide the analysis and search for specific content within the AI related legal documents located in the `/data` directory. These thematic areas provide a structured framework for understanding and categorizing information pertinent to the overarching goal of the repository. Each thematic area file may include the following sections:

#### Definitions:

This section outlines key terms and concepts relevant to the specific thematic area. It provides a clear understanding of the terminology used and establishes a foundation for interpreting information within the context of the defined themes.

#### Identification:

The Identification section delineates the criteria and indicators used to recognize and assess relevant content within AI related legal documents. It guides users on how to identify specific elements or patterns that align with the thematic focus, ensuring a systematic and standardized approach to document analysis.

#### Considerations:

Considerations highlight additional factors or aspects that users should take into account when analyzing documents within the specified thematic area. These may include nuanced perspectives, potential challenges, or particular contexts that could influence the interpretation of information.

These thematic areas serve as invaluable tools for researchers and analysts, offering a structured methodology to streamline the analysis of AI related legal documents related to Artificial Intelligence. By providing clear definitions, identification guidelines, and considerations, these files enhance the efficiency and accuracy of the document analysis process.


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
