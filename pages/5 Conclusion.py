import streamlit as st
import requests 
from streamlit_lottie import st_lottie

st.title(':blue book: :blue[Conclusion]')

st.write(
 """
 
In conclusion, the analysis of the national high school exam scores from 2018 to 2021 provides valuable insights into the performance trends of students during these years. Here are some key findings:

* Overall Performance Trends: The dashboard shows how scores have changed from year to year. It helps to provide us the candidate quality and exam difficulty to improve.

* Analyzing the score of Subjects, Blocks, and Combos: It provides the insight for student to select based on their strenghths and weaknesses and helps make plan revise better.

* Geographical Disparities: We can see big differences in scores between different provinces or cities. Understanding these geographical gaps can help address educational inequalities and provide direction and assistance to struggling areas.

Overall, the analysis of the national high school exam scores provides valuable insights into the educational landscape and highlights areas that require attention and intervention to ensure the continuous improvement of the education system.
 """
)



def load_lottieurl(url: str):
 r = requests.get(url)
 if r.status_code != 200:
    return None
 return r.json()
lottie_school = load_lottieurl(
 "https://lottie.host/8937418e-9e58-4fb7-85c7-2857144f0776/dcZjmV9IJZ.json"
)
st_lottie(lottie_school, height=500)