import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)

import streamlit as st
from dotenv import load_dotenv

from src.data.pdfs import PDFManager
from src.data.text import TextManager
from src.chatbot.conversation import ConversationManager
from src.data.vectorstore import VectorStoreManager
from htmlTemplate import css, bot_template, user_template


def handle_user_question(question, conversation):
    response = conversation({"question": question})
    return response


def main():
    load_dotenv()
    st.set_page_config(
        page_title="Chat with multiple PDFs",
        page_icon=":books:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.write(css, unsafe_allow_html=True)
    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question")
    if user_question:
        # ai_answer = ConversationManager.handle_user_question(user_question, st.session_state.conversation)
        ai_answer = handle_user_question(user_question, st.session_state.conversation)
        st.session_state.chat_history = ai_answer['chat_history']
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    with st.sidebar:
        st.subheader("Your PDFs")
        documents = st.file_uploader("Upload a PDF", accept_multiple_files=True, type="pdf")
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = PDFManager().get_text_from_multiple_pdfs(documents)
                chunks = TextManager().get_chunks_from_text(raw_text)
                vectorstore = VectorStoreManager().get_vectorstore(chunks)
                st.session_state.conversation = ConversationManager().get_conversation(vectorstore)


if __name__ == '__main__':
    main()
