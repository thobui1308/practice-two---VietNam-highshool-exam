import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title(":bar_chart: Dataset")
st.write(
 """
 The data is about score of Vietnam Highschool Examination which is annually hold by the ministry of education for highschool student. 
 This exam will determine the chance to be accepted by different universities in Vietnam. 
 In the Vietnamese high school education system, students are often required to choose a specific combination of subjects based on their interests or career aspirations. 

*   **BlockA**: This combination typically includes subjects related to natural sciences. It consists of ***Math, Physics, and Chemistry***. Students who aim for engineering, science, or medical fields usually opt for this combination.
*   **BlockA1**: Similar to Khoi A but with a variation. It includes ***Math, Physics, and a Foreign Language (usually English)***. This variation is often chosen by students interested in technical or scientific fields who also prioritize proficiency in English.
*   **BlockB**: This combination focuses on subjects related to biology and is often chosen by students interested in life sciences or medical studies. It comprises ***Math, Chemistry, and Biology.***
*   **BlockC**: This combination emphasizes subjects related to social sciences and humanities. It typically includes ***Literature, History, and Geography.*** Students interested in fields like law, social sciences, or humanities usually opt for this combination.
*   **BlockD**: This combination is a mix of subjects from both natural sciences and social sciences/humanities. It includes ***Math, Literature, and a Foreign Language (usually English)***. It provides a balanced approach and is chosen by students with varied interests or those unsure about their career paths.

And, we use Natural Sciences and Social Sciences as combinations used for graduation evaluation:
*   **Natural Sciences**: This combination, known as the Natural Sciences Group, comprises ***Physics, Chemistry, and Biology.*** It's designed for students undergoing graduation evaluation who have chosen to focus on natural sciences. 
*   ***Social Sciences***: This combination, known as the Social Sciences and Humanities Group, includes ***History, Geography, and Civic Education.*** It's intended for students undergoing graduation evaluation who have selected subjects from the social sciences and humanities.
 """
)

tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs(["Data", "2017","2018","2019","2020","2021"])
with tab1:
    df = pd.read_parquet('df_sample.parquet')
    st.dataframe(df.head(20))
with tab2:
    df = pd.read_parquet('df_2017.parquet')
    st.dataframe(df.head(20))
with tab3:
    df = pd.read_parquet('df_2018.parquet')
    st.dataframe(df.head(20))
with tab4:
    df = pd.read_parquet('df_2019.parquet')
    st.dataframe(df.head(20))
with tab5:
    df = pd.read_parquet('df_2020.parquet')
    st.dataframe(df.head(20))
with tab6:
    df = pd.read_parquet('df_2021.parquet')
    st.dataframe(df.head(20))


