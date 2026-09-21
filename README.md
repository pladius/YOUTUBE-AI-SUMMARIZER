# YouTube Video Q&A & Summarizer

An AI-powered **YouTube transcript Q&A and summarization tool** built with Python, Streamlit, LangChain, and OpenRouter.

## Overview

This project allows users to enter a YouTube video URL and ask questions or request summaries based on its transcript.

## Features

* 🎥 Extract YouTube video transcripts
* 🤖 Ask questions about video content
* 📝 Generate AI-powered summaries
* 🔗 LangChain-based processing pipeline
* 🖥️ Simple and interactive Streamlit UI
* ⚠️ Basic error handling

## Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **OpenRouter**
* **YouTube Transcript API**

## Workflow

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
LangChain Prompt
     ↓
OpenRouter LLM
     ↓
AI-Generated Response
```

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run YoutubeVideoLoader.py
```

## Example

**YouTube URL**

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

**Query**

```text
Summarize this video.
```

The application processes the transcript and generates a response based on the user's request.

## Project Structure

```text
YouTube-Video-Loader/
│
├── YoutubeVideoLoader.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Project Purpose

This project was built to practice **LLM integration, LangChain workflows, transcript processing, and Streamlit application development**.
