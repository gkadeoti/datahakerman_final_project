## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Love Island Twitter Sentiment Prediction')

author.properties.friends = st.number_input('followers', 0, 3000)
author.properties.status_count = st.number_input('statuscount', 0, 3000)
author.properties.verified = st.selectbox('verified', options=['True','False'])
content.body = st.text_area('Tweet to analyze')
location.country = st.selectbox('country', options=['GG','GB','JE','IM'])
properties.sentiment = st.selectbox('sentiment', options=['-1.','0.','1.'])
location.latitude = st.number_input('latitude degrees', -90, 90)


input_data_dict = {
    'author.properties.friends': 2345,
    'author.properties.status_count': 135,
    'author.properties.verified': True,
    'content.body': LoveIsland is the biggest show in Europe right now!!
   # 'location.country':'GB',
   # 'location.latitude': 53.3887
}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = "output"

save_model_predictor = TabularPredictor.load(save_path) #unnecessary

submit = st.button("CLICK HERE TO PREDICT TWEET SENTIMENT")

if submit:
    sentiment_prediction = save_model_predictor.predict(input_data)[0]
    st.write(f"The tweet sentiment prediction is: {sentiment_prediction}")