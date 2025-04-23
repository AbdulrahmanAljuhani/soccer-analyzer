%%writefile app.py
import streamlit as st
import requests

# --- Static default content ---
default_question = "Is this Salem Al-Dawsari or another Al-Hilal winger?"
default_answer = """
Based on the movement pattern provided, the player moves gradually forward across the pitch, maintaining consistent lateral positioning. 
This behavior is characteristic of a winger making progressive runs. Given the movement data and typical playstyle, it's likely to be a winger such as **Salem Al-Dawsari**.
"""

# --- UI ---
st.title("⚽ AI Soccer Player Analyzer")

st.markdown("### Ask a question about this player's movement:")
st.text_area("Question:", value=default_question, height=120, disabled=True)

st.markdown("### ✅ AI's Answer:")
st.success(default_answer)
