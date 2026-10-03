# gemma-ai-assistant
🤖 Gemma AI Assistant — LangChain + Ollama + Streamlit

A local AI assistant built with LangChain, Ollama, Gemma 2B, and Streamlit. The project also uses LangSmith for tracing and monitoring LangChain executions.

✨ Features
🤖 Gemma 2B local LLM
🦜 LangChain integration
🦙 Ollama for running the model locally
🎨 Custom Streamlit UI
💬 Interactive question-answer interface
📊 LangSmith tracing and monitoring
⚡ Simple LangChain prompt → model → output pipeline
🛠️ Technologies Used
Python
LangChain
Ollama
Gemma 2B
Streamlit
LangSmith
python-dotenv
🏗️ How It Works
User Question
      ↓
Streamlit UI
      ↓
ChatPromptTemplate
      ↓
LangChain Chain
      ↓
Ollama
      ↓
Gemma 2B
      ↓
StrOutputParser
      ↓
AI Response

LangSmith tracks the LangChain execution and provides information about prompts, model calls, inputs, outputs, and execution time.

📸 Screenshots
🤖 Application

📊 LangSmith Traces

🔍 LangSmith Run Details

⚙️ Requirements

Before running the project, make sure you have:

Python 3.10+
Ollama
Gemma 2B
LangChain
Streamlit
