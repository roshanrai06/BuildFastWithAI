from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# Setup
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMy27HigcmeWrH__DvPe_ygyuklqio_mo"
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template=tweet_template, input_variables=['number', 'topic'])
google_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
tweet_chain = tweet_prompt | google_gemini

# UI
st.title("🧠 AI Tweet Generator")
st.caption("Powered by Gemini 1.5 Flash")

topic = st.text_input("💬 Topic")
number = st.number_input("📝 Number of tweets", min_value=1, max_value=10, value=3, step=1)

if st.button("Generate Tweets"):
    topic = topic.strip()
    if topic:
        with st.spinner("Generating tweets..."):
            response = tweet_chain.invoke({"number": number, "topic": topic})
            tweets = response.content.strip().split("\n\n")

        st.success("Done! Here are your tweets:")
        for idx, tweet in enumerate(tweets, 1):
            st.markdown(f"**{idx}.** {tweet.strip()}")
    else:
        st.warning("⚠️ Please enter a topic.")
