import streamlit as st
import requests

# --- Default content ---
default_question = "Is this Salem Al-Dawsari or another Al-Hilal winger?"
default_answer = (
    "Based on the movement pattern provided, the player moves gradually forward across the pitch, "
    "maintaining consistent lateral positioning. This behavior is characteristic of a winger making progressive runs. "
    "Given the movement data and typical playstyle, it's likely to be a winger such as **Salem Al-Dawsari**."
)

# --- UI Layout ---
st.title("⚽ AI Soccer Player Analyzer")

# --- AI's Answer (shown first) ---
st.markdown("### AI's Insight:")
st.markdown(
    f"""
    <div style='background-color: #262730; padding: 20px; border-radius: 8px; color: #e1e1e1; font-size: 16px;'>
        {default_answer}
    </div>
    """,
    unsafe_allow_html=True
)

# --- Editable Question ---
st.markdown("### Ask something about the player's movement:")
st.text_area("Question:", value=default_question, height=120)
