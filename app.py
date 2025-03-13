import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

# Heading
st.header("Simple Retrieval Augmented Generation Application")

# Input from user
input_text = st.text_input("Post your question here👇")

# Setting the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the queries asked by the user"),
    ("user", "{question}")]
)

# Initializing llm llama3.2 through ollama
llm = Ollama(model = "llama3.2")

# Output parser -> Process/Cleans out the output
output_parser = StrOutputParser()

# This is the pipeline for this project. (This Flow is followed.)
chain = prompt|llm|output_parser

# User input
if input_text:
    st.write(chain.invoke(input_text))
