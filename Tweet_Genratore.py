from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

os.environ["GOOGLE_API_KEY"] = "AIzaSyDMy27HigcmeWrH__DvPe_ygyuklqio_mo"
tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number', 'topic'])
google_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
tweet_chain = tweet_prompt | google_gemini

st.header("Tweet Generator")
st.subheader("Generate Tweets using Generative AI")
topic = st.text_input("Enter a topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)
if st.button("Generate Tweets"):
    if topic:
        response = tweet_chain.invoke({"number": number, "topic": topic})
        st.text_area("Generated Tweets", value=response.content, height=300)
    else:
        st.warning("Please enter a topic.")
