from flask import Flask, render_template, request, jsonify
import openai
import os
from datetime import datetime

openai.api_key_path = "openai_api_key.txt"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    selected_model = "text-davinci-003"

    tokens = max(prompt.count(" ") * 24, 24)
    generated_text = ""

    response = openai.Completion.create(
        model=selected_model,
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        temperature=0.4,
)

    generated_text = response.choices[0].text.strip()

    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    logfile = "logs/" + current_time + ".txt"
    with open(logfile, "x") as f:
        f.write("Model: " + selected_model +'\n\nPrompt: ' + prompt + '\n\n' + 'Generated text: ' + generated_text)

    return {"generated_text": generated_text}


if __name__ == "__main__":
    app.run(debug=True)
