from dotenv import load_dotenv
load_dotenv()  # Load all the environmental variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our API Key
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Function to load Google Gemini Model and provide query as response
def get_gemini_response(question: str, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrive query from the sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)

    return rows

# Define your prompt

prompt = [
    '''
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS \n \n
    For Example, \n
    Example-1: How many entries of records are present?,
    the SQL command will be something like SELECT COUNT(*) FROM STUDENT; \n
    Example-2: Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science"; \n
    Also the sql code should not have ``` in beginning or end and sql word in the output
    '''
]


# Streamlit App

st.set_page_config(page_title = 'I can retrive any SQL query')
st.header('Gemini App to retrive SQL Data')

question = st.text_input("Input: ", key = 'input')

submit = st.button("Ask the question")

# If Submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, 'student.db')
    st.subheader('The Respose is')

    for row in data:
        print(row)
        st.header(row)
