from openai import OpenAI
from dotenv import load_dotenv
import os
import random
from roles import roles

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_question(role, asked):
    topic = random.choice([t for t in roles[role]["topics"] if t not in asked])
    prompt = f"""{roles[role]["intro"]}\nAsk one question about: {topic}"""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    question = response.choices[0].message.content  # ✅ This is the correct way
    return question, topic

def evaluate_answer(question, answer):
    prompt = f"""You are an expert interviewer. The question is:
"{question}"
The candidate answered:
"{answer}"

Give feedback, rate the answer from 1 to 10, and suggest improvements if any."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    feedback = response.choices[0].message.content  # ✅ Correct way here too
    return feedback
