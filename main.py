from flask import Flask, render_template, request
import openai
import os

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    generated_text = response.choices[0].text.strip()
    return render_template("result.html", generated_text=generated_text)



if __name__ == "__main__":
    app.run(debug=True)
