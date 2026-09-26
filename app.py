
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI CHATBOT")
st.caption("Hiii! Ask me anything.")

api_key = st.secrets["GEMINI_API_KEY"]

text = st.text_input("Ask me anything")

if st.button("Send"):
    if text.strip():
        with st.spinner("Thinking..."):

            url = (
                "https://generativelanguage.googleapis.com/"
                "v1beta/models/gemini-2.5-flash:generateContent"
            )

            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": api_key
            }

            data = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": text
                            }
                        ]
                    }
                ]
            }

            response = requests.post(
                url,
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                result = response.json()
                answer = result["candidates"][0]["content"]["parts"][0]["text"]
                st.write(answer)
            else:
                st.error("API error. Please check your API key and try again.")

    else:
        st.warning("Please enter a question.")
```
