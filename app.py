from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


def getDate():
    return datetime.now().strftime("%Y-%d-%m")


@app.route("/")
def home():
    return render_template("layout.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    query = request.form["query"]
    if query != "":
        url = f"https://newsapi.org/v2/everything?q={query}&from={getDate()}&sortBy=publishedAt&apiKey={os.getenv("NEWS_API")}"
        req = requests.get(url)
        return render_template("result.html", news=json.loads(req.text))
    return render_template("layout.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
