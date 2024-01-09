<img src="README.png" alt="drawing" width="300"/>

# AI Document Analysis

## AI Legal Document Analysis

Automate the analysis of AI-related legal documents with this repository. 

Explore diverse thematic areas within the expansive field of Artificial Intelligence (AI) legislation, including related terms like 'machine learning' or 'algorithmic modeling.' Leveraging language models, the repository extracts insights, aiming to contribute to a global index of AI accountability.

**Versatile Functionality:** Customize the analysis for AI-related legal documents, allowing users to focus on multiple user-defined thematic areas with flexibility.

Explore, analyze, and advance accountability in the dynamic landscape of AI-related legalities.

## Why Use This Repository?

Simplify the search for specific thematic areas in extensive AI-related legal documents, addressing challenges associated with manually exploring complex global legal frameworks. 

By automating the analysis of diverse texts from different countries, the tool streamlines the identification of relevant information in the field of AI, providing researchers and professionals with a powerful tool to extract valuable insights from a wide range of legal documents.

The complexity of AI legislation, dispersed in multilingual and nuanced texts, makes the manual search for thematic areas time-consuming and challenging. This repository, powered by language models, significantly alleviates this burden by automating the extraction of relevant content. It empowers users to efficiently identify and comprehend specific aspects of AI legislation, promoting a more accessible and accelerated understanding of global AI regulations.

The repository's primary goal is to democratize access to crucial information in AI-related legal texts, fostering a collaborative environment where researchers, policymakers, and enthusiasts can contribute to and benefit from a collective understanding of global AI regulations.


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

**Note**: Currently, the content of the document should be in a UTF-8 encoded text file. Future updates may extend support for URLs or PDFs from which text extraction will be performed.

### Data Check - Thematic Areas

Thematic Areas, located within the `/datachecks` directory, are Markdown files tailored to facilitate the analysis and search for specific content within AI-related legal documents found in the `/data` directory. Serving as structured frameworks, these thematic areas guide the understanding and categorization of information, aligning with the repository's overarching goal.



## Output Information

Upon analysis, the script generates a CSV file in the `/dataoutputs` directory. The file structure includes answers to the following questions along with additional information:

1. Identify the thematic area outlined in the markdown guide for analysis.
2. Determine if the document precisely addresses the topic of artificial intelligence, referencing the provided definition.
3. Conclusively establish if the document addresses the identified thematic area, providing a detailed explanation.
4. Provide a detailed explanation of how the document addresses the specified thematic area, including references to the relevant chapter and article.

Additional Columns:
- `data_file`: Name of the analyzed data file.
- `data_check_file`: Name of the thematic area markdown guide file.
- `prompt`: Prompt used for analysis.
- `ai_model`: Selected AI model for analysis.
- `date`: Date and time of the analysis.

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

- Allow multiple data inputs (web documents, PDFs).
- Enable simple customization of the data output format, providing users the flexibility to choose the desired output structure.
- Include a troubleshooting section with common issues users might encounter and solutions.
- Highlight any security considerations or best practices, especially when dealing with sensitive AI documents.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
