import streamlit as st
import json
import pandas as pd
from PIL import Image
from ast import literal_eval
import os
import re

st.set_page_config(layout="wide")
#st.title('Flights Rich Data')
st.markdown("<h1 style='text-align: center; color: white;'>Flights Rich Data</h1>", unsafe_allow_html=True)


json_file_path = "csvjson_new.json"
#image_files = os.listdir("images")
#print(image_files)


with open(json_file_path, 'r',encoding='utf-8') as j:
     flights_data = json.loads(j.read())

col1, col2 = st.columns([2,1])

@st.cache()
def get_data(json_data):
    flights_df = pd.DataFrame(flights_data) 
    airlines_list = flights_df['Name'].values
    return flights_df, airlines_list
    
#airlines = ['Indigo','Air Asia','Srilankan Airlines','Vistara','Go Air','Akasa Air','Spicejet']
flights_df, airlines_list = get_data(flights_data)
with col1:
    airline_selected = st.selectbox('Select Airline',airlines_list)

def get_airline_attributes(airline):
    if airline in airlines_list:
        airline_data = flights_df.loc[flights_df['Name']==airline]
        airline_data = airline_data.T
        airline_data.reset_index(inplace=True)
        airline_data.columns=['Attribute','Value']
        return airline_data
    else:
        return "No attributes present for the airline"

#def display_airline_image(airline):
    



airline_data = get_airline_attributes(airline_selected)
with col1:
    st.table(airline_data)
#display_airline_image(airline_selected)
# res = [x for x in image_files if re.search(airline_selected.lower(), x)]
res = airline_data.loc[airline_data['Attribute']=='Image Link']['Value'].values[0]
#print(type(res))
res = literal_eval(res)
#print(type(res))
with col2:
    for img in res:
        #print(img)
        image = Image.open("images/airline_images/" + img)
        st.image(image)


