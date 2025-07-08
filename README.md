# RAG_v0.5
### A Python-based Retrieval-Augmented Generation (RAG) system using LangChain, Hugging Face, and Pinecone. This project demonstrates how to build a simple question-answering assistant that leverages document retrieval and LLMs to answer user queries based on the content of a provided PDF.
## Features
- `Retrieval-Augmented Generation:` Answers are generated using both a language model and context retrieved from your documents.
- `PDF Document Support:` Loads and splits a PDF into chunks for embedding and retrieval.
- `Vector Database:` Uses Pinecone for fast, scalable vector search.
- `Hugging Face Integration:` Utilizes Hugging Face models for both embeddings and text generation.
- `Interactive CLI:` Ask questions in a loop; type exit to quit.

## Setup
1. `Python Version`
  - Requires Python 3.13 (see .python-version).

2. `Install Dependencies`
``` bash
pip install -r requirements.txt
# or, if using pyproject.toml:
pip install .
```

3. `Environment Variables`
Create a .env file in the project root with the following variables:
```.env
# Hugging Face API token (required for model and embeddings)
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

# Pinecone API key (required for vector database)
PINECONE_API_KEY=your_pinecone_api_key_here
```

4. `Prepare Your Data`
- Place your PDF file in the assets/ directory (default: RAG_CLIENT_FILE.pdf).
- You can change the file path in helper.py if needed.

5. `Start the Assistant`
``` git-bash
uv run main.py (if you are using uv)
OR
python main.py 
```
- Type your question at the prompt.
- Type `exit` to quit.

## Open for Collaboration

I welcome contributions, suggestions, and new ideas! If you'd like to collaborate, open an issue or pull request, or reach out via GitHub. Whether it's bug fixes, new features, or documentation improvements, your input is appreciated.
