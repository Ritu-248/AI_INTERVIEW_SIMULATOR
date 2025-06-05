# 🎤 AI Interview Simulator – Powered by OpenAI & Streamlit

This is a smart, interactive **AI-based Interview Simulator** built using **Streamlit** and **OpenAI GPT-3.5 Turbo**. It simulates real technical interviews for different roles like Python Developer, Data Analyst, and Frontend Developer. The app dynamically asks questions, evaluates user answers, provides instant feedback, and stores results for future review.



## 🚀 Demo


---![Screenshot 2025-06-05 153447](https://github.com/user-attachments/assets/6de557d4-eac6-4bb3-81f0-728ea37397c0)
![Screenshot 2025-06-05 143801](https://github.com/user-attachments/assets/7c7e47b6-261e-4bec-92ad-9624ca72bcef)
![Screenshot 2025-06-05 153310](https://github.com/user-attachments/assets/92479365-9f9f-479c-8147-8faa6dacff53)

[interview_results.csv](https://github.com/user-attachments/files/20606970/interview_results.csv)
[Uploading AI INTERVIEW SIMULATOR.zip…]()





## 🧠 Features

✅ Role-based technical interview questions (Python, Frontend, Data Analyst)  
✅ Input answers via **text** or **voice**  
✅ Instant **feedback and rating** using GPT-3.5  
✅ **Speech-to-text** using `speechrecognition`  
✅ Stores all answers, feedback, and scores in a CSV  
✅ Option to retry or restart the interview  
✅ Clean and responsive **Streamlit UI**

---

## 🛠️ Tech Stack

- **Streamlit** – for UI
- **OpenAI GPT-3.5 Turbo** – for question generation & evaluation
- **Python-dotenv** – for API key management
- **SpeechRecognition** – for voice input (optional)
- **Pandas** – for CSV data logging

---

## 📁 Project Structure

📦 AI-Interview-Simulator
├── app.py # Main Streamlit app
├── .env # API key (ignored by Git)
├── .gitignore # Ignores .env and CSV
├── requirements.txt # All dependencies
├── roles.py # Role-wise interview topics
├── interview_logic.py # GPT-powered Q&A logic
├── utils.py # Speech-to-text logic
├── interview_results.csv # Stores results (auto-generated)


---

## 📦 Setup Instructions

### 1. Clone the Repository

bash

git clone https://github.com/your-username/ai-interview-simulator.git
cd ai-interview-simulator

2. Install Dependencies
pip install -r requirements.txt

4. Set Up .env
Create a .env file with your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

4. Run the App
streamlit run app.py

🎯 Interview Roles Supported
Python Developer – OOP, Decorators, APIs, etc.

Data Analyst – SQL, Excel, Visualization, Stats

Frontend Developer – HTML, CSS, JS, React

📑 Output Format
Every response is stored in interview_results.csv like this:

Name	Role	Topic	Question	Answer	Feedback	Rating
John Doe	Python Developer	OOP in Python	"What is OOP?"	"..."	"You answered well..."	8


🛡️ Security Notes
.env is listed in .gitignore to protect your API key

Interview logs are stored locally in CSV (you can integrate a DB or cloud sheet for scaling)

📜 License
MIT © [RITU PRIA]

🙌 Acknowledgements
OpenAI

Streamlit

SpeechRecognition

💡 Pro Tip: Host this app on Streamlit Cloud and add the demo link to your resume or LinkedIn profile to showcase your AI + Full Stack skills!


