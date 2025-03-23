# News-Sentiment-Tts

## Overview
This project fetches news articles based on a company name, analyzes sentiment, and converts text to speech using Hindi TTS. It consists of:
- **Web Scraper**: Extracts news headlines from Google News.
- **Sentiment Analysis**: Uses `transformers` to determine the sentiment of each headline.
- **Text-to-Speech (TTS)**: Converts text to Hindi speech using `google-tts`.
- **Fast API**: Provides API endpoints for fetching news and generating speech.
- **Gradio UI**: A simple and faster user interface for interaction.

## 🛠️ Installation
First, install dependencies:
```bash
pip install -r requirements.txt
python api.py
gradio run app.py
