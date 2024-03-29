import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

#read data
df = pd.read_parquet('practice-two---VietNam-highshool-exam\dataset\df_sample.parquet')
##
st.title(':books: Vietnam Highschool Exam 2018-2021 Dashboard')
st.markdown('##')

#Overview
@st.cache_data
def compute_statistics(df):
    subjects = ['Math', 'Literature', 'ForeignLanguage', 'Chemistry', 'Biology', 'Physics', 'History', 'Geography', 'CivicEducation']
    total_student = len(df)
    total_score_10 = df[subjects].apply(lambda x: (x == 10).any(), axis=1).sum()
    total_failed = df[subjects].apply(lambda x: (x <= 1).any(), axis=1).sum()

    return total_student, total_score_10, total_failed

total_student, total_score_10, total_failed = compute_statistics(df)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.info('Total Student:')
    st.subheader("{:,} :student:".format(total_student))
with middle_column:
    st.info('Total Score 10:')
    st.subheader('{:,} :+1: :100:' .format(total_score_10))
with right_column:
    st.info('Total Failed:')
    st.subheader('{:,} :writing_hand::sob:' .format(total_failed))
st.markdown('---')

st.write('**Compare scores of subjects over the years**')
left_column, right_column = st.columns(2)
with left_column:
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['Math', 'Literature', 'ForeignLanguage', 'Chemistry', 'Biology', 'Physics', 'History', 'Geography', 'CivicEducation'])
    with tab1:
        fig = px.box(df, x='Year', y='Math', title = 'Subject', 
                labels = {'value': 'Math', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab2:
        fig = px.box(df, x='Year', y='Literature', title = 'Subject', 
                labels = {'value': 'Literature', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab3:
        fig = px.box(df, x='Year', y='ForeignLanguage', title = 'Subject', 
                labels = {'value': 'ForeignLanguage', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab4:
        fig = px.box(df, x='Year', y='Chemistry', title = 'Subject', 
                labels = {'value': 'Chemistry', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab5:
        fig = px.box(df, x='Year', y='Biology', title = 'Subject', 
                labels = {'value': 'Biology', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab6:
        fig = px.box(df, x='Year', y='Physics', title = 'Subject', 
                labels = {'value': 'Physics', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab7:
        fig = px.box(df, x='Year', y='History', title = 'Subject', 
                labels = {'value': 'History', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab8:
        fig = px.box(df, x='Year', y='Geography', title = 'Subject', 
                labels = {'value': 'Geography', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab9:
        fig = px.box(df, x='Year', y='CivicEducation', title = 'Subject', 
                labels = {'value': 'CivicEducation', 'Year':'Year'})
        st.plotly_chart(fig)

with right_column:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['BlockA', 'BlockA1', 'BlockB', 'BlockC', 'BlockD'])
    with tab1:
        fig = px.box(df, x='Year', y='BlockA', title = 'Block', 
                color_discrete_sequence=['red'],   
                labels = {'value': 'BlockA', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab2:
        fig = px.box(df, x='Year', y='BlockA1', title = 'Block', 
                color_discrete_sequence=['red'],   
                labels = {'value': 'BlockA1', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab3:
        fig = px.box(df, x='Year', y='BlockB', title = 'Block', 
                color_discrete_sequence=['red'],   
                labels = {'value': 'BlockB', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab4:
        fig = px.box(df, x='Year', y='BlockC', title = 'Block', 
                color_discrete_sequence=['red'],   
                labels = {'value': 'BlockC', 'Year':'Year'})
        st.plotly_chart(fig)
    with tab5:
        fig = px.box(df, x='Year', y='BlockD', title = 'Block', 
                color_discrete_sequence=['red'],   
                labels = {'value': 'BlockD', 'Year':'Year'})
        st.plotly_chart(fig)
###
st.write('**Compare score distribution of subjects over years**')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['Math', 'Literature', 'ForeignLanguage', 'Chemistry', 'Biology', 'Physics', 'History', 'Geography', 'CivicEducation'])
with tab1:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Math', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab2:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Literature', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab3:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='ForeignLanguage', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab4:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Chemistry', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab5:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Biology', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab6:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Physics', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab7:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='History', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab8:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='Geography', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab9:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='CivicEducation', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Subject Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


st.write('Compare score distribution of blocks over the years')
tab1, tab2, tab3, tab4, tab5 = st.tabs(['BlockA', 'BlockA1', 'BlockB', 'BlockC', 'BlockD'])
with tab1:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='BlockA', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Block Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab2:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='BlockA1', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Block Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab3:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='BlockB', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Block Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab4:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='BlockC', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Block Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
with tab5:
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 2))
    sns.kdeplot(data=df, x='BlockD', hue='Year', fill=False, alpha=0.5)
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Block Score Distribution from 2018 to 2021')
    plt.grid(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

