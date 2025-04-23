import streamlit as st
import requests

API_KEY = "38d6531b293afee64eb66fd256b9182b016b64235930677a513b69f65aaa2177"
MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

tracking_data = {
    "frame_15.jpg": {"position": [197, 125]},
    "frame_30.jpg": {"position": [315, 140]},
    "frame_45.jpg": {"position": [340, 145]},
    "frame_60.jpg": {"position": [360, 150]},
    "frame_75.jpg": {"position": [375, 153]},
    "frame_90.jpg": {"position": [400, 160]},
}

def build_prompt(question, data):
    prompt = "You are an AI soccer analyst. These are tracked player positions:\n\n"
    for frame, info in data.items():
        prompt += f"- {frame}: Position {info['position']}\n"
    prompt += f"\nAnswer this: {question}"
    return prompt

def ask_ai(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "prompt": prompt[-2000:],
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 0.9,
    }
    response = requests.post("https://api.together.xyz/v1/completions", json=data, headers=headers)

    try:
        result = response.json()
        print("✅ Together API result:", result)
        return result["choices"][0]["text"].strip()
    except Exception as e:
        print("❌ API error:", response.text)
        return "⚠️ AI failed to respond. Check your model/API key or logs for details."

# UI
st.title("⚽ AI Soccer Player Analyzer")
q = st.text_area("Ask an AI about a soccer player's movement.")
if st.button("Ask AI"):
    st.write("⏳ Thinking...")
    prompt = build_prompt(q, tracking_data)
    answer = ask_ai(prompt)
    st.success(answer)
