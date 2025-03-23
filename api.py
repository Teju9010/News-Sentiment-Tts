
from fastapi import FastAPI, Query
from scraper import fetch_news
from sentiment import analyze_sentiment
from tts import text_to_speech
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI News Sentiment & TTS API is running!"}

@app.get("/news")
def get_news(company: str = Query(..., description="Company name to fetch news for")):
    articles = fetch_news(company)

    if not articles:
        return {"error": "No news articles found."}

    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])

    return {"articles": articles}

@app.post("/tts")
def generate_tts(text: str):
    filename = text_to_speech(text)
    return FileResponse(filename, media_type="audio/mp3", filename="speech.mp3")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

