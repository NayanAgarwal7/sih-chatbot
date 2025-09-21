from flask import Flask, render_template, request, jsonify
from responses import get_response
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json.get("message")
    bot_reply = get_response(user_msg)

    # Log conversation
    with open("chat_logs.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([user_msg, bot_reply])

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
