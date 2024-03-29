import streamlit as st
import requests 
from streamlit_lottie import st_lottie

st.title(':school: Conclusion')

st.write(
 """
 
In conclusion, the analysis of the national high school exam scores from 2018 to 2021 provides valuable insights into the performance trends of students during these years. Here are some key findings:

* Overall Performance Trends: The overall performance of students in the national high school exam has shown variations over the years. It is essential to delve deeper into the reasons behind these fluctuations to identify areas for improvement and implement effective educational strategies.

* Subject-specific Analysis: Analyzing the scores across different subjects reveals areas of strength and weakness among students. This information can guide educational institutions and policymakers in curriculum development and resource allocation.

* Geographical Disparities: There may be noticeable differences in exam scores across different provinces or regions. Understanding these geographical disparities can help in addressing educational inequalities and providing targeted support to underperforming areas.
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