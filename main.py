from langchain_chain import get_few_shot_db_chain
import streamlit as st

st.title("Classic Models: Database Q&A")

question = st.text_input("Type your Question") 

if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    st.header("Answer:")
    st.write(answer)

