import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.llms import ctransformers
from langchain_community.llms import CTransformers


## Function to get response from the LLama 2 Model

#Start of the function
def get_LLama_Response(input_text, no_of_words, essay_style):
    # Calling LLama 2 Model
    llm = CTransformers(model='E:\\Machine learning Project\\LLM Lama\\Model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})

    # Prompt Template
    template = """
        Write an essay for {essay_style} job profile on the topic {input_text}
        within {no_of_words} words.
    """
    prompt = PromptTemplate(input_variables=['essay_style', 'input_text', 'no_of_words'], template=template)

    # Generate the response from the LLama 2 Model
    response = llm(prompt.format(essay_style=essay_style, input_text=input_text, no_of_words=no_of_words))
    print(response)
    return response


## End of the Function


st.set_page_config(page_title="Generate Essays",
                   page_icon="🌟",
                   layout="centered",
                   initial_sidebar_state="collapsed"
                   )

st.header("Generate Essays 🌟")

input_text = st.text_input("Enter the Essay Topic")

## Creating more colomns for additional 2 fields 

col1 , col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input("No of Words")

with col2:
    essay_style = st.selectbox("Writing the essay for",
                           ('Researchers', 'Students', 'Teachers', 'Common People'), index=0)

Submit = st.button("Generate")


## Final Response
if Submit:
    st.write(get_LLama_Response(input_text , no_of_words ,  essay_style ))