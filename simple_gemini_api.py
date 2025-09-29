from flask import Flask, jsonify
import generativeai as genai
import os

app = Flask(__name__)

# Get Gemini API key from environment variable
API_KEY = os.environ.get("GENIE_API_KEY")
if not API_KEY:
    raise ValueError("Please set the GENIE_API_KEY environment variable!")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Static prompt
STATIC_PROMPT = "Write a short poem about AI and humans."

@app.route("/generate", methods=["GET"])
def generate_content():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=STATIC_PROMPT
        )
        return jsonify({"generated_text": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Render sets PORT automatically
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
