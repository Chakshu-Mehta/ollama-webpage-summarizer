# SummarAIze

A Python project that summarizes webpage content using a locally running open-source LLM via Ollama.

## Features
- Extracts text from webpages
- Uses a local LLM for summarization
- No paid API required
- Markdown-style summaries

## Tech Stack
- Python
- Ollama
- BeautifulSoup
- Requests

## Installation

Install dependencies:# Ollama Webpage Summarizer

A Python-based AI project that extracts content from webpages and generates concise summaries using a **locally running open-source Large Language Model (LLM)** via **Ollama**.

This project demonstrates how to integrate **web scraping with LLM inference** to build a simple AI-powered summarization tool without relying on paid APIs.

---

## Features

- Extracts clean text from webpages
- Uses a **local LLM model (Llama 3.2)** via Ollama
- Generates intelligent summaries
- Works completely offline after model download
- Handles scraping errors gracefully
- Simple CLI interface

---

## Demo Workflow

User Input → Web Scraper → Clean Text → LLM (Ollama) → Summary Output

1. User provides a webpage URL  
2. The program scrapes the webpage content  
3. The content is cleaned and structured  
4. The content is sent to a local LLM  
5. The LLM generates a summary  

---

## Tech Stack

- Python  
- Ollama  
- Llama 3.2 (Local LLM)  
- BeautifulSoup  
- Requests  
- IPython Markdown Display  

---

## Project Structure

```
ollama-webpage-summarizer
│
├── app.py                # Main program
├── scraper.py            # Web scraping logic
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Ignored files
```

---

## Installation

### 1 Install Python Dependencies

```
pip install -r requirements.txt
```

Dependencies include:

```
requests
beautifulsoup4
ollama
ipython
```

---

### 2 Install Ollama

Download Ollama from:

https://ollama.com

Verify installation:

```
ollama --version
```

---

### 3 Download LLM Model

```
ollama pull llama3.2
```

---

## Running the Application

Run the main script:

```
python app.py
```

Enter a webpage URL when prompted:

```
Enter webpage URL: https://example.com
```

Example output:

```
------ SUMMARY ------

Example.com is a demonstration website used for testing purposes. 
It contains minimal content intended to illustrate how a webpage 
might look and function.
```

---

## Example URLs for Testing

These sites work well with the scraper:

```
https://example.com
https://cnn.com
https://anthropic.com
https://edwarddonner.com
https://python.org
```

Some websites may block automated scraping and return **403 errors**.

---

## How It Works

### Step 1 — Web Scraping

The program fetches webpage HTML using the `requests` library with browser-like headers.

### Step 2 — Content Cleaning

Using **BeautifulSoup**, scripts and styles are removed and only readable text is extracted.

### Step 3 — Prompt Construction

A structured prompt is sent to the LLM containing the webpage text.

### Step 4 — LLM Summarization

The **Llama 3.2 model** running locally through Ollama generates a summary.

---

## Key Learning Outcomes

This project demonstrates:

- LLM integration using local models
- Web scraping pipelines
- Prompt engineering
- Building AI-powered tools with Python
- Running inference locally without APIs

---

## Limitations

- Some websites block scraping (403 Forbidden)
- Summaries depend on webpage text quality
- Large webpages may require truncation

---

## Future Improvements

Potential enhancements:

- Build a **Streamlit web interface**
- Add **multi-style summaries** (bullet points / short / detailed)
- Implement **RAG pipeline for better summarization**
- Add **multi-page summarization**
- Export summaries to **Markdown / PDF**

---

## Author

Chakshu  
B.Tech CSE (AI & Data Science)

Learning focus:
- Large Language Models
- AI Engineering
- Generative AI systems

---

## License

This project is licensed under the MIT License.
