♻️ ReUseAI
ReUseAI is a lightweight, AI-powered web app that helps users find beginner-friendly and eco-conscious ways to reuse everyday objects in creative DIY fashion. Simply enter an object (like a jar, t-shirt, or bottle), and the app generates 5 simple reuse ideas using Google’s Gemini 1.5 Flash API.

🚀 Features
🔎 Enter any common object and get reuse suggestions

🤖 Powered by Gemini 1.5 Flash (Google Generative AI API)

🌱 Focus on DIY and sustainability

⚡ Fast, minimalist Flask-based backend

🧠 Uses Markdown formatting for clean response rendering

🛠 Tech Stack
Python 3.7+

Flask (Backend Web Framework)

Gemini 1.5 Flash via google-generativeai

Jinja2 (HTML Templating)

python-dotenv (Environment Variables)

markdown (Render AI response as HTML)

HTML/CSS (UI template provided)

📦 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/reuseai.git
cd reuseai
Install dependencies

bash
Copy
Edit
pip install flask google-generativeai python-dotenv markdown
Get your Gemini API key

Visit: https://makersuite.google.com/app/apikey

Create a .env file in the project root:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Run the app

bash
Copy
Edit
python app.py
🧠 How It Works
User inputs the name of an object.

App generates a prompt asking Gemini to return 5 easy and sustainable reuse ideas.

Gemini responds in Markdown, which is converted to HTML and displayed in the UI.

💡 Use Cases
Build your own AI-powered sustainability tools

Customize the prompt to generate donation ideas, recycling tips, or upcycling tutorials

Use as a foundation for educational eco apps

📘 Example
Input: "Plastic Bottle"
Output:

Cut it into a funnel for gardening use

Turn into a bird feeder with a few holes

Use for storing homemade cleaning supplies

Make a drip irrigation system

Craft it into a pen holder

📈 What's Next?
Improve response formatting with icons or images

Add save/share/export functionality

Integrate more AI APIs (e.g. for detecting object names from photos)