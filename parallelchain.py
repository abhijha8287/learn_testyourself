from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
import streamlit as st
# Load environment variables
load_dotenv()
st.title("Learn and test yourself")
model1 = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)
model2 = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)
parser = StrOutputParser()

# Step 1: Prompt to generate notes from topic
prompt1 = PromptTemplate(
    template='write a detailed note on {topic}',
    input_variables=['topic']
)

# Step 2: Prompt to generate questions from notes
prompt2 = PromptTemplate(
    template='Generate 5 questions from the following \n {text}',
    input_variables=['text']
)

# Step 3: Prompt to merge notes and questions
prompt3 = PromptTemplate(
    template='Merge the provided notes and questions in single document \n notes -> {notes} and questions -> {questions}',
    input_variables=['notes', 'questions']
)

# Step 1 Chain
notes_chain = prompt1 | model1 | parser

# Step 2 Chain (take notes output, pass as text)
questions_chain = (
    RunnableLambda(lambda x: {"text": x}) |
    prompt2 | model2 | parser
)

# Step 3 Chain (merge notes and questions)
merge_chain = (
    RunnableLambda(lambda x: {"notes": x["notes"], "questions": x["questions"]}) |
    prompt3 | model2 | parser
)
topic = st.text_input("Enter your topic")
# Final chain: step by step execution
def full_chain(inputs):
    notes = notes_chain.invoke(inputs)                        # topic -> notes
    questions = questions_chain.invoke(notes)                 # notes -> questions
    merged = merge_chain.invoke({"notes": notes, "questions": questions})
    return merged

# Run it


if st.button('Enter'):
    # Step 1: Generate detailed report
    result = full_chain({topic})
    st.write(result)