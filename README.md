# AskMyDocs

`AskMyDocs` is a minimal retrieval-augmented generation (RAG) demo for asking questions about a local text file from the terminal. It uses LangChain to load and split a document, OpenAI embeddings to vectorize the chunks, FAISS for similarity search, and an OpenAI chat model to answer questions using only the retrieved context.

## What It Does

- Loads a local document from `data/sample.txt`
- Splits the document into small overlapping chunks
- Builds a FAISS vector index from those chunks
- Retrieves the top matching chunks for each question
- Sends the retrieved context to `gpt-4.1-nano`
- Runs as a simple command-line chat loop

## Tech Stack

- Python
- LangChain
- OpenAI Embeddings
- OpenAI Chat Completions via `ChatOpenAI`
- FAISS
- `python-dotenv`

## How It Works

The app in `app.py` follows this flow:

1. Load environment variables from `.env`
2. Read `data/sample.txt`
3. Split the document with:
   - `chunk_size=300`
   - `chunk_overlap=50`
4. Create embeddings with `OpenAIEmbeddings()`
5. Store the vectors in FAISS
6. Retrieve the top `3` relevant chunks for each question
7. Ask the model to answer only from the retrieved context

## Project Structure

```text
AskMyDocs/
├── app.py
├── reequirnments.txt
├── .env
└── data/
    └── sample.txt
```

## Prerequisites

- Python 3.10+
- An OpenAI API key
- Internet access for OpenAI API calls

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r reequirnments.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
python app.py
```

You will see:

```text
Ask questions about your document. Type 'exit' to quit.
```

Example:

```text
You: What did Archit work on before learning AI tools?
Bot: Archit worked on a European energy utility platform and handled billing, reconciliation, SQL analysis, Dynamics AX, and backend workflows.
```

Type `exit` to stop the program.

## Customizing The Document

To ask questions about your own content, replace the text inside `data/sample.txt` with your document content.

If you want to use a different file, update this line in `app.py`:

```python
loader = TextLoader("data/sample.txt")
```

## Current Limitations

- Supports only a single local text file
- Rebuilds the FAISS index every time the app starts
- No persistence for embeddings or vector store
- No support for PDFs, DOCX files, or folders of documents
- No chat history memory beyond the current question

## Notes

- The dependency file is currently named `reequirnments.txt`, so the install command in this README uses that exact filename.
- The model configured in the app is `gpt-4.1-nano`.
- The app prompt explicitly tells the model to answer only from retrieved context.

## Possible Next Improvements

- Add support for PDFs and multiple files
- Persist the FAISS index to disk
- Add a web UI with Streamlit or FastAPI
- Make the document path configurable
- Add source citations in responses

