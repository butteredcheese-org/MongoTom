from flask import Flask, render_template, request
import openai
import os

openai.api_key_path = "openai_api_key.txt"
app = Flask(__name__)

chat_history = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    chat_id = request.form.get("chat_id")  # use get() method instead

    if chat_id is None:
        return "Chat ID is missing"  # handle missing chat ID

    if chat_id not in chat_history:
        chat_history[chat_id] = []

    tokens = prompt.count(" ") * 24
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        temperature=0.4,
    )
    generated_text = response.choices[0].text.strip()

    return render_template("result.html", generated_text=generated_text, chat_history=chat_history[chat_id])


#if __name__ == "__main__":
app.run(debug=False)
