import streamlit as st
import requests

api_key = 'APIKEY'
url = 'https://api.nasa.gov/planetary/apod?' \
      f'api_key={api_key}'

request = requests.get(url)
content = request.json()

title = content['title']
image_url = content['hdurl']
text = content['explanation']



st.set_page_config(layout="centered")
intro = 'Space of the day'
st.markdown(f"<h1 style='text-align: center; color: grey;'>{intro}</h1>",
            unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>",
            unsafe_allow_html=True)
c1, c2, c3 = st.columns([0.2, 1, 0.2])
with c2:
      st.image(image_url)
st.write(text)