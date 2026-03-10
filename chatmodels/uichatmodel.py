# import streamlit as st
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
# load_dotenv()
# st.set_page_config(
#     page_title="Funny AI Chatbot",
#     page_icon="🤖",
#     layout="centered"
# )

# st.title("🤖 Funny AI Chatbot")

# model = ChatMistralAI(
#     model="mistral-small-2506",
#     temperature=0.9
# )


# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage(content="You are a funny AI agentt.")
#     ]


# for msg in st.session_state.messages:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("user"):
#             st.markdown(msg.content)

#     elif isinstance(msg, AIMessage):
#         with st.chat_message("assistant"):
#             st.markdown(msg.content)


# prompt = st.chat_input("Type your message...")

# if prompt:
#     st.session_state.messages.append(HumanMessage(content=prompt))

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = model.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))

#     with st.chat_message("assistant"):
#         st.markdown(response.content)




# mood bot 
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------- Custom UI ----------
st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:700;
text-align:center;
}

.default{
background:#e2e3ff;
color:#1a1443;
}

.mode-badge{
padding:6px 14px;
border-radius:20px;
font-weight:600;
display:inline-block;
margin-bottom:10px;
}

.funny{
background:#fff3cd;
color:#856404;
}

.sad{
background:#d4edda;
color:#155724;
}

.sarcastic{
background:#f8d7da;
color:#721c24;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-title">🤖 AI Personality Chatbot</p>', unsafe_allow_html=True)
st.caption("Talk to an AI with different personalities")

# ---------- Sidebar ----------
st.sidebar.title("🎭 Personality Mode")

mode_option = st.sidebar.radio(
    "Choose AI personality:",
    ["Default", "Funny", "Sad", "Sarcastic"]
)

# Mode prompts
if mode_option == "Default":
    system_prompt = "You are a helpful AI assistant who gives clear, informative, and friendly responses."
    badge = '<span class="mode-badge default">🤖 Default Mode</span>'

elif mode_option == "Funny":
    system_prompt = "You are a funny AI assistant who replies with humor, jokes, and playful tone."
    badge = '<span class="mode-badge funny">😆 Funny Mode</span>'

elif mode_option == "Sad":
    system_prompt = "You are a sad AI assistant who replies emotionally and empathetically."
    badge = '<span class="mode-badge sad">😢 Sad Mode</span>'

else:
    system_prompt = "You are a sarcastic AI assistant who replies with witty sarcasm and playful roasting."
    badge = '<span class="mode-badge sarcastic">😏 Sarcastic Mode</span>'

# Reset chat button
if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=system_prompt)]

# Display badge
st.markdown(badge, unsafe_allow_html=True)

# ---------- Model ----------
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# Update system prompt if mode changes
if st.session_state.messages[0].content != system_prompt:
    st.session_state.messages = [SystemMessage(content=system_prompt)]

# ---------- Chat Display ----------
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# ---------- Chat Input ----------
user_prompt = st.chat_input("Type your message...")

if user_prompt:

    st.session_state.messages.append(HumanMessage(content=user_prompt))

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking... 🤖"):

            response = model.invoke(st.session_state.messages)

            reply = response.content

            st.markdown(reply)

    st.session_state.messages.append(AIMessage(content=reply))