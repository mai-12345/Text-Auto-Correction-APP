import streamlit as st
from textblob import TextBlob
st.title("Auto-Correction of Text")

#text area
text=st.text_area("Enter Your Text....",height=100)

def correct_text(text):
    model=TextBlob(text)
    corrected_text=model.correct()
    return corrected_text

if st.button('Correct Text'):
    if text:
         st.write(correct_text(text))
    else:
        st.write('Please, Enter a text to correct.')
