
## This is going to be a Streamlit App

import streamlit as st

st.title('Love Island Online Sentiment Prediction')

author.properties.friends  = st.number_input ('number of friends', 0, 8000)
author.properties.status_count = st.number_input ('status_count', 0, 12000)
author.properties.verified = st.selectbox('verified', options=['Yes','No'])
content.body = st.text_area('post content')
location.country = st.selectbox('country', options=['GB','GG','JE','IM'])
location.longitude = st.number_input ('longitude')
location.latitude = st.number_input ('latitude')

