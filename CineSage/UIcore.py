import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

st.set_page_config(
    page_title="Movie Extractor AI",
    page_icon="🎬"
)

st.title("🎬 Movie Information Extractor AI")
st.caption("Extract important movie details from a paragraph")

# Initialize model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.3,
    max_tokens=400
)

# Prompt
prompt = ChatPromptTemplate([
    ("system",
"""
You are a professional movie information extractor.

Your task : to give ectracted information from a movie description paragraph in a structured and clean format. give short summaray of the movie sas well in clean and readable format and also add if you think this movie has something more othe rthan the mentioned details okayy.

From the given paragraph extract:

Movie Name
Release Year
Director
Genre
Main Cast
Plot / Story Premise
Themes
Notable Features
Setting

Also generate a short summary (2-3 sentences).

Return the answer in a clean readable format.
"""
),
("human","{paragraph}")
])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Paste movie paragraph here...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role":"user","content":user_input})

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Analyzing movie... 🎥"):

            final_prompt = prompt.invoke({"paragraph": user_input})
            response = model.invoke(final_prompt)

            answer = response.content

            st.markdown(answer)

    st.session_state.messages.append({"role":"assistant","content":answer})




