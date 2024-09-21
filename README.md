# Chatbot Comparison Project: LangChain vs LlamaIndex

## Introduction

### RAG (Retrieval-Augmented Generation)

RAG, or Retrieval-Augmented Generation, is a new approach in AI that mixes large language models (LLMs) with information from external sources. This method helps AI systems give more accurate and up-to-date answers.

In a RAG system:
1. Information is pulled from an external database or source.
2. This information is combined with the user's question.
3. The LLM uses both to create a more informed and accurate response.

RAG systems are great for chatbots and virtual assistants because they can give answers based on real-time information, going beyond the limitations of pre-trained models.

![RAG Diagram](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DZwcPDr0z3QghwxG_H7qnQ.png)

*Figure 1: Conceptual diagram of a RAG system*

## Project Overview

This project aims to build and compare chatbots using two popular AI frameworks: LangChain and LlamaIndex. The goal is to explore the differences, pros, and cons of each framework when building RAG-based chatbots.

## Goals

1. Build a chatbot using LangChain.
2. Build a similar chatbot using LlamaIndex.
3. Compare the performance, ease of use, and features of both frameworks.
4. Document key differences and ideal use cases for each framework.

## Project Structure
```bash
RAG_PROJECT
├── Data
│   └── pride_and_prejudice.txt
├── Notebooks
│   ├── langchain-prototype.ipynb
│   ├── llama-index-prototype.ipynb
│   └── storage
│       ├── default__vector_store.json
│       ├── docstore.json
│       ├── graph_store.json
│       ├── image__vector_store.json
│       └── index_store.json
├── README.md
├── faiss_index
│   ├── index.faiss
│   └── index.pkl
└── requirements.txt

## Installation

1. Make sure you have pyenv installed.
2. Clone this repository:
```
git clone https://github.com/elviramg/rag_project.git cd rag_project
```
3. Activate the virtual environment:
4. Install the project dependencies:
```
pip install -r requirements.txt
```
5. Set up environment variables:
- Create a `.env` file at the root of the project.
- Add the necessary variables, such as the OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```
6. You are now ready to run the notebooks and project scripts.
