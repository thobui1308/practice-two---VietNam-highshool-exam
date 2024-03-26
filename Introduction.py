import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events

st.set_page_config(layout="wide")

st.title(':blue[Vietnam Highschool Exam 2017 to 2021 Analytic] 📖')
st.write (
    """
    The National High School Exam in Vietnam is one of the most critical milestones for students. 
    The score from this examination not only determines the completion of high school education but also decides if students can get into universities. 
    Therefore, in this practice, I will analyze the data on National High School Examination scores from 2017 to 2021. 
    The main goal with this project is to learn how to make a dashboard using Streamlit, an open-source library that is perfectly suited for Data Science. 
    And by doing this, I hope to gain a deep and detailed understanding of secondary education in VietNam. 
    """
)

def load_lottieurl(url: str):
 r = requests.get(url)
 if r.status_code != 200:
    return None
 return r.json()
lottie_school = load_lottieurl(
 "https://lottie.host/dd34bbd2-3cf6-498c-b98f-53f2d1903742/sDXVsuisQJ.json"
)
st_lottie(lottie_school, height=500)
