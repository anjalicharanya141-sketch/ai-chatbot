import streamlit as st
from google import genai

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI CHATBOT")
st.caption("Hiii! Ask me anything.")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

text = st.text_input("Ask me anything")

if st.button("Send"):
    if text.strip():
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=text
            )

        st.write(response.text)
    else:
        st.warning("Please enter a question.")
