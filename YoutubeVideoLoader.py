#Libraries
import os
import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_community.document_loaders import YoutubeLoader

#--------------------------------------------------------
#Streamlit
st.title ("Youtube Video Loader/Summarizer")
st.subheader("Please Input your text")
user_url = st.text_input("Please enter a url:   ")
user_query = st.text_input ("Please enter your query: ")
#-----------------------------------------------------------

#Loader

if user_url.startswith(("https://www.youtube.com/", "https://youtu.be/")):
    try:
        loader = YoutubeLoader.from_youtube_url(
            user_url,
            add_video_info=False
        )

        doc = loader.load()

        st.success("Video loaded successfully!")

    except Exception:
        st.error("This video couldnt be loaded please try again.")

#--------------------------------------------------------------

#LLM
os.environ ["OPENAI_API_KEY"] = "YOUR-KEY"

llm = ChatOpenAI(
    model = "openai/gpt-5.6-sol",
    base_url = "https://openrouter.ai/api/v1",
    max_tokens = 500
)
#------------------------------------------------------------------

#Output
info_prompt = PromptTemplate.from_template(
    "Do the command instructed by the user {user_query_var} about a youtube transcript : {doc}"
)

chain = info_prompt | llm

if user_query:

    response = chain.invoke({
        "user_query_var": user_query,
        "doc": doc
    })
    print (response.content)
    st.subheader("Ouput: ")
    st.write (response.content)

