import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ==============================
# Load Environment Variables
# ==============================

load_dotenv()


# ==============================
# LangSmith Tracking
# ==============================

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# ==============================
# Streamlit Page Configuration
# ==============================

st.set_page_config(
    page_title="Gemma AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# ==============================
# Custom CSS
# ==============================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e1b4b 50%,
            #312e81 100%
        );
        color: white;
    }

    /* Main container */
    .block-container {
        max-width: 850px;
        padding-top: 60px;
    }

    /* Title */
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 40px;
    }

    /* Input label */
    label {
        color: #f8fafc !important;
        font-weight: 600 !important;
    }

    /* Input container */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 2px solid #818cf8 !important;
        border-radius: 12px !important;
    }

    /* Input text */
    div[data-baseweb="input"] input {
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        font-size: 17px !important;
        font-weight: 500 !important;
        background-color: #ffffff !important;
    }

    /* Placeholder text */
    div[data-baseweb="input"] input::placeholder {
        color: #6b7280 !important;
        opacity: 1 !important;
    }

    /* Response outer box */
    .response-box {
        margin-top: 30px;
        padding: 28px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            rgba(59, 130, 246, 0.18),
            rgba(168, 85, 247, 0.18)
        );
        border: 1px solid rgba(129, 140, 248, 0.6);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.30);
    }

    /* Response heading */
    .response-title {
        font-size: 21px;
        font-weight: 700;
        color: #c4b5fd;
        margin-bottom: 15px;
    }

    /* Response text */
    .response-text {
        font-size: 17px;
        line-height: 1.7;
        color: #f8fafc;
        white-space: pre-wrap;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 50px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# Prompt Template
# ==============================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Please respond to the question asked"
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)


# ==============================
# Header
# ==============================

st.markdown(
    '<div class="title">🤖 Gemma AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Powered by LangChain + Ollama + Gemma 2B</div>',
    unsafe_allow_html=True
)


# ==============================
# User Input
# ==============================

input_text = st.text_input(
    "💬 Ask your question",
    placeholder="Type your question here..."
)


# ==============================
# Ollama Gemma 2B Model
# ==============================

llm = Ollama(model="gemma:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


# ==============================
# Generate Response
# ==============================

if input_text:

    with st.spinner("✨ Gemma is thinking..."):

        response = chain.invoke(
            {"question": input_text}
        )

    st.markdown(
        f"""
<div class="response-box">
    <div class="response-title">✨ AI Response</div>
    <div class="response-text">{response}</div>
</div>
""",
        unsafe_allow_html=True
    )


# ==============================
# Footer
# ==============================

st.markdown(
    """
<div class="footer">
    Built with ❤️ using LangChain & Ollama
</div>
""",
    unsafe_allow_html=True
)