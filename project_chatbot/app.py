#!/usr/bin/python3
from flask import Flask, render_template, request, jsonify
from chat import get_response  # This should be your LLM logic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])  # Changed to match frontend
def predict():
    try:
        data = request.get_json()
        text = data.get("message")
        if not text:
            return jsonify({"error": "No message provided"}), 400
        
        response = get_response(text)
        # Ensure response is in string format
        answer = str(response) if response else "I didn't get a response from the AI."
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)