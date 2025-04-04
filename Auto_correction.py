import streamlit as st
from textblob import TextBlob
from langchain.document_loaders import PyPDFLoader
import tempfile


st.title("Auto-Correction of Text")

options=st.selectbox('Uploaded A File or Write A Text,Choose an Option...',('Write A Text','Upload File'))

if options=='Write A Text':
    #text area
    text=st.text_area("Enter Your Text....",height=100)

elif options=='Upload File':
#upload pdf file
    upload_file = st.file_uploader('Choose File...', type = ['pdf'])
    
    if upload_file is not None:
        def extract_text_from_pdf(upload_file):

            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf_file:
                temp_pdf_file.write(upload_file.read())
                tempfile_path = temp_pdf_file.name

            loader = PyPDFLoader(tempfile_path)
            documents = loader.load()  

            text = ""
            for doc in documents:
                text += doc.page_content + "\n"

            return text.strip()

        text = extract_text_from_pdf(upload_file)
        st.success('PDF Processed Successfuly.')
    # st.write(text)

def correct_text(text):
    model=TextBlob(text)
    corrected_text=model.correct()
    return corrected_text

if st.button('Correct Text'):
    if text:
         st.write(correct_text(text))
    else:
        st.write('Please, Enter a text to correct.')
