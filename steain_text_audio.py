import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

st.title("🗣️ Text to Speech App (with gTTS)")

text = st.text_area("Enter text to speak")

if st.button("🔊 Speak"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        tts = gTTS(text=text, lang='en')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        st.audio(mp3_fp, format='audio/mp3')
        st.success("Speaking completed.")
