import streamlit as st
import ollama

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI CHATBOT")
st.caption("Hiii! Ask me anything.")

text = st.text_input("Ask me anything")

if st.button("Send"):
    if text.strip():
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )

        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a question.")