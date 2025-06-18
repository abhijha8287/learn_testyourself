# 📚 Learn and Test Yourself

An intelligent assistant that helps you **learn any topic** by generating concise notes and testing your understanding with questions — all in one go!

🌐 **Live App**: [learntestyourself.streamlit.app](https://learntestyourself.streamlit.app/)

> ⚠️ If the app is asleep, simply refresh or click “Wake App” to activate it — this is how Streamlit Cloud manages free-tier resources.

---

## 🧠 What Does This App Do?

This AI-powered tool takes any topic you input and performs the following steps:

1. 📝 **Generates Detailed Notes**  
2. ❓ **Creates 5 Practice Questions** from the notes  
3. 📄 **Combines Notes and Questions** into a single document

---

## ✅ Features

- Built with **LangChain** and **OpenAI GPT-4**
- Three-step chained processing:
  1. Topic → Notes  
  2. Notes → Questions  
  3. Notes + Questions → Final document
- Simple, clean **Streamlit** user interface
- Helpful for students, educators, and self-learners

---

## ⚙️ Tech Stack

| Component           | Tool/Library               |
|--------------------|----------------------------|
| Frontend           | [Streamlit](https://streamlit.io) |
| LLM Backend        | [OpenAI GPT-4](https://platform.openai.com) |
| Orchestration      | [LangChain](https://www.langchain.com) |
| Prompt Chaining    | `PromptTemplate` + `RunnableLambda` |
| Output Formatting  | `StrOutputParser` |
| Env Management     | `python-dotenv` |

