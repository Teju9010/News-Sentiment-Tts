import gradio as gr
import requests

API_URL = "https://teju9010-news-sentiment.hf.space"

def fetch_news_and_generate_speech(company):
    response = requests.get(f"{API_URL}/news", params={"company": company})

    if response.status_code != 200:
        return "Error fetching news.", None 

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return f"Invalid response: {response.text}", None

    if "error" in data:
        return data["error"], None

    display_text = ""
    for article in data.get("articles", []):
        display_text += f"**Title:** {article['title']}\n"
        display_text += f"**Sentiment:** {article['sentiment']}\n\n"

    
    tts_response = requests.post(f"{API_URL}/tts", json={"text": display_text})
    if tts_response.status_code == 200:
        return display_text, tts_response.content  # Returns text + audio
    return display_text, "TTS Failed"

with gr.Blocks() as demo:
    gr.Markdown("# News Sentiment & TTS App")

    with gr.Row():
        company_input = gr.Textbox(label="Enter Company Name")
        fetch_button = gr.Button("Fetch News & Generate Speech")

    news_output = gr.Textbox(label="News Sentiment Output", interactive=False)
    tts_audio = gr.Audio(label="Generated Speech")

    fetch_button.click(fetch_news_and_generate_speech, inputs=company_input, outputs=[news_output, tts_audio])

demo.launch()


