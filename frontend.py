import streamlit as st
import requests
import json

st.header("somma le API")
st.write("hello world!")

num1 = st.number_input('addendo 1')
num2 = st.number_input('addendo 2')

reqUrl = "http://localhost:8000/sum"

h = {
 "Accept": "*/*",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "num1": num1,
  "num2": num2
})

response = requests.request("POST", reqUrl, data=payload, headers=h)


st.markdown(f'''## Somma nel frontend:
            {num1 + num2}''')

st.markdown(f'''## Somma nell'API:
            {response.text}''')
