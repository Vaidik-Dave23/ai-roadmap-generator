import requests
import streamlit as st


def Prompt(user_Goal, user_Time):
    return [
        {"role": "system","content": """
You are a helpful assistant that help users make a proper Roadmap to achive their goals in Time
Give:
1. Monthly roadmap
2. Weekly breakdown
3. TODAY'S TASK (very important)
4. What to build at each stage
5. Common mistakes

Rules:
- Be practical
- No fluff
- Focus on execution
- Make it realistic

Make it practical and realistic.
"""},
        {"role": "user","content": f"Goal: {user_Goal}, Time: {user_Time}"
        }
    ]


def ai(prompt):
    API_KEY="eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjMwMDA5OTRAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.cqFXOjLqW9xzH-Z-GyRzfQX9ba2drNxJMyT4Y7-B65M"
    url="https://aipipe.org/openrouter/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
        }
    data={
        "model": "openai/gpt-4.1-nano",
        "messages": prompt
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']



def output(response):
    print(response)




st.title("AI Roadmap Generator")

goal = st.text_input("Enter your goal:")
time = st.text_input("Time to complete (e.g., 2 months):")

if st.button("Generate Roadmap"):
    if goal and time:
        with st.spinner("Generating roadmap..."):
            messages = Prompt(goal, time)
            result = ai(messages)
            st.write(result)
    else:
        st.warning("Please enter both goal and time.")