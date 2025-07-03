import streamlit as st
import pyttsx3

# Streamlit UI
st.title("🗣️ Text to Speech App")
text = st.text_area("Enter text to speak")

# Create pyttsx3 engine
engine = pyttsx3.init()

if st.button("🔊 Speak"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Speak the text
        engine.say(text)
        engine.runAndWait()
        st.success("Speaking completed.")
