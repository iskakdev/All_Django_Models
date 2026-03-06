import streamlit as st
import requests
from all_projects.all_projects_app.views import mobile_processor_list


def check_mobile_price():
    api_url = 'http://127.0.0.1:8000/mobile_predict/'

    st.title('Mobile Price Project')

    rating = st.number_input('Rating: ', min_value=0.0, step=1.0)
    num_ratings = st.number_input('Number Ratings: ', min_value=0, step=1)
    ram = st.number_input('RAM: ', min_value=0, step=1)
    rom = st.number_input('ROM: ', min_value=0, step=1)
    back_cam = st.number_input('Back Camera: ', min_value=1, step=1)
    front_cam = st.number_input('Front Camera: ', min_value=1, step=1)
    battery = st.number_input('Battery: ', min_value=1, step=1)
    processor = st.selectbox('Processor: ', options=mobile_processor_list)
    scrap_date = st.selectbox('Scrape Date: ', ['2023-06-17'])

    mobile_data = {
        "Rating": rating,
        "Num_Ratings": num_ratings,
        "RAM": ram,
        "ROM": rom,
        "Back_Cam": back_cam,
        "Front_Cam": front_cam,
        "Battery": battery,
        "Processor": processor,
        "Scrap_Date": scrap_date
    }

    if st.button('Send'):
        try:
            answer = requests.post(api_url, json=mobile_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Error: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Fail to connection')
