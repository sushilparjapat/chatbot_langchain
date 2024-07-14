
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
import os

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="gemini-pro")
## Langmith tracking

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Define a PromptTemplate for question answering
prompt = PromptTemplate(
    template="The question is: {question}. Can you answer it?",
    input_variables=["question"]
)

st.title('Langchain Demo With gemini-pro API')
input_text = st.text_input("Search the topic you want")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        st.write(chain.invoke({'question': input_text}))
    except AttributeError as e:
        st.error(f"An error occurred: {str(e)}")



