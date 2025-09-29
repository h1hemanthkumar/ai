from flask import Flask, jsonify
from google import generativeai as genai
import os

app = Flask(__name__)

# Get Gemini API key from environment variable
API_KEY = os.environ.get("GENIE_API_KEY")
if not API_KEY:
    raise ValueError("Please set the GENIE_API_KEY environment variable!")

# Configure API key globally
genai.configure(api_key=API_KEY)

# Static prompt
STATIC_PROMPT = "Write a short poem about AI and humans."

@app.route("/generate", methods=["GET"])
def generate_content():
    try:
        # Generate content using the new API
        response = genai.models.generate(
            model="gemini-2.5-pro",
            prompt=STATIC_PROMPT
        )
        return jsonify({"generated_text": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
