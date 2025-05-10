import os
import markdown
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    user_input = None

    if request.method == 'POST':
        user_input = request.form.get('object_name')
        if user_input:
            prompt = f"""Give 5 simple and eco-friendly ways to recycle or reuse a {user_input}. Respond in short bullet points. Make it beginner-friendly and easy to read. Avoid long paragraphs."""
            try:
                chat = model.start_chat()
                gemini_response = chat.send_message(prompt)
                response = gemini_response.text

                response = markdown.markdown(response)

            except Exception as e:
                response = f"Error communicating with Gemini: {e}"

    return render_template('index.html', response=response, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)