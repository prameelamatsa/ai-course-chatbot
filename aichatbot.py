import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="AI Course Chatbot", page_icon="🤖", layout="centered"
)

st.title("🤖 AI Course Assistant")
st.write(
    "Welcome to your Week 1 AI Internship project with Skillinf! Ask me anything"
    " about courses or AI."
)

# Initialize the Gemini client securely using Streamlit Secrets
try:
  client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
  st.error(
      "API Key not found! Please add your GEMINI_API_KEY in Streamlit Secrets."
  )
  client = None

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display prior chat messages when the app reruns
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Accept user input from the chat box
if prompt := st.chat_input("Type your question here..."):
  # Add user message to session state and display it
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Generate and display the assistant's response
  with st.chat_message("assistant"):
    if client:
      with st.spinner("Thinking..."):
        try:
          # Call the Gemini model
          response = client.models.generate_content(
              model="gemini-3.8-flash",
              contents=prompt,
          )
          bot_reply = response.text
          st.markdown(bot_reply)

          # Save assistant response to session state
          st.session_state.messages.append(
              {"role": "assistant", "content": bot_reply}
          )
        except Exception as e:
          st.error(f"An error occurred: {e}")
    else:
      st.warning(
          "Please configure your API key in Streamlit Secrets to enable"
          " responses."
      )
