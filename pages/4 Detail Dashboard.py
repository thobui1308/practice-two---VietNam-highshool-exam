import pandas as pd
import streamlit as st

st.title(':mag: :bookmark_tabs: VietNam Highschool Exam Dashboard')
#Load data
@st.cache_data
def load_data(file):
    df = pd.read_parquet(file)
    return df

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is None:
    st.stop()

df = load_data(uploaded_file)
with st.expander("Data Preview"):
    st.dataframe(df.head(10))

#Side bar
st.sidebar.header("Please Filter Here:")
##Create filter
province_options = list(df['ProvinceName'].unique())
selected_province = st.sidebar.multiselect(
    "Select the Province:",
    options=province_options,
    default=[]  
)
if not selected_province:
    df_filtered = df.copy()  
else:

    df_filtered = df[df['ProvinceName'].isin(selected_province)]


#Overview
@st.cache_data
def compute_statistics(df_filtered):
    subjects = ['Math', 'Literature', 'ForeignLanguage', 'Chemistry', 'Biology', 'Physics', 'History', 'Geography', 'CivicEducation']
    total_student = len(df_filtered)
    total_score_10 = df_filtered[subjects].apply(lambda x: (x == 10).any(), axis=1).sum()
    total_failed = df_filtered[subjects].apply(lambda x: (x <= 1).any(), axis=1).sum()

    return total_student, total_score_10, total_failed

total_student, total_score_10, total_failed = compute_statistics(df_filtered)

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

# Data Visualization
import matplotlib.pyplot as plt
#Barchart 
subjects = ['Math', 'Literature', 'ForeignLanguage', 'Chemistry', 'Biology', 'Physics', 'History', 'Geography', 'CivicEducation']
blocks = ['BlockA', 'BlockA1', 'BlockB', 'BlockC', 'BlockD']
combos = ['NaturalSciences', 'SocialSciences']
average_scores_subjects = df_filtered[subjects].mean()
average_scores_blocks = df_filtered[blocks].mean()
average_scores_combos = df_filtered[combos].mean()

##subject 
overall_average_score = df[subjects].mean()
fig1, ax1 = plt.subplots()
bars1 = ax1.bar(subjects, average_scores_subjects, color='skyblue')

ax1.plot(subjects, overall_average_score, color='red', marker='o', linestyle='')

for bar, score in zip(bars1, average_scores_subjects):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, round(score, 2),
            ha='center', va='bottom', fontsize=9, color='black')

for x, y in zip(subjects, overall_average_score):
    ax1.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=9, color='red')
ax1.set_ylabel('Average Score')
ax1.set_title('Average Scores by Subject')
ax1.grid(False)
plt.xticks(rotation=45) # Rotate x-axis labels

##block
overall_average_block = df[blocks].mean()
fig2, ax2 = plt.subplots()
bars2 = ax2.bar(blocks, average_scores_blocks, color='skyblue')

ax2.plot(blocks, overall_average_block, color='red', marker='o', linestyle='')

for bar, score in zip(bars2, average_scores_blocks):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, round(score, 2),
            ha='center', va='bottom', fontsize=9, color='black')

for x, y in zip(blocks, overall_average_block):
    ax2.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=9, color='red')
ax2.set_ylabel('Average Score')
ax2.set_title('Average Scores by Block')
ax2.grid(False)

##combo
overall_average_combo = df[combos].mean()
fig3, ax3 = plt.subplots()
bars3 = ax3.bar(combos, average_scores_combos, color='skyblue')

ax3.plot(combos, overall_average_combo, color='red', marker='o', linestyle='')

for bar, score in zip(bars3, average_scores_combos):
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, round(score, 2),
            ha='center', va='bottom', fontsize=9, color='black')

for x, y in zip(combos, overall_average_combo):
    ax3.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=9, color='red')
ax3.set_ylabel('Average Score')
ax3.set_title('Average Scores by Combination')
ax3.grid(False)

# Visualize
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.pyplot(fig1)

with middle_column:
    st.pyplot(fig2)

with right_column:
    st.pyplot(fig3)

#Distrubition 
import numpy as np
##subject
### Create select box
selected = st.selectbox('Please select a subject', subjects)
if selected:
    df_selected = df_filtered[selected]
    fig, ax = plt.subplots(figsize=(8, 2))
    bins = np.arange(0, 10.5, 0.25)  # Create bins with distance 0.25
    counts, bins, _ = ax.hist(df_selected, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    ax.set_xticks(np.arange(0, 10.25, 1))  # Set ticks for x axis with distance 1
    ax.set_xlabel('Score')
    ax.set_ylabel('Number of Students')
    ax.set_title(f'Score Distribution of {selected}')
    ax.grid(False)
    
    # Displays the number of students 
    for i in range(len(bins) - 1):
        ax.text(bins[i] + 0.125, counts[i] + 1, str(int(counts[i])), ha='center', va='top', fontsize=4,rotation=90)

    st.pyplot(fig)
    with st.expander("Infomation Details"):
        total_students = df_selected.count().sum()
        average_score = np.mean(df_selected)
        total_10_scores = np.sum(df_selected == 10) 
        below_average = len(df_selected[df_selected <= 1])
        below_5 = len(df_selected[df_selected < 5])
        most_common_score = round(df_selected.mode().iloc[0], 2)

        st.write(f"Total number of students: {total_students:,}")
        st.write(f"Average score: {average_score:.2f}")
        st.write(f"Number of students scoring 10: {total_10_scores:,}")
        st.write(f"Number of students failing (having a score below or equal to 1): {below_average:,}")
        st.write(f"Number of students scoring below average (having a score below 5): {below_5:,}")
        st.write(f"Most common score achieved by students: {most_common_score:.2f}")

##block
selected_block = st.selectbox('Please select a block', blocks)
if selected_block:
    df_selected_block = df_filtered[selected_block]
    fig2, ax2 = plt.subplots(figsize=(13, 5))
    bins = np.arange(0, 31, 1) 
    counts, bins, _ = ax2.hist(df_selected_block, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    ax2.set_xticks(np.arange(0, 31, 1))
    ax2.set_xlabel('Socre')
    ax2.set_ylabel('Number of Students')
    ax2.set_title(f'Score Distribution by {selected_block}')
    ax2.grid(False)
    
    # Displays the number of students 
    for i in range(len(bins) - 1):
        ax2.text(bins[i] + 0.125, counts[i] + 1, str(int(counts[i])), ha='left', va='bottom', fontsize=6,rotation=90)

    st.pyplot(fig2)
    with st.expander("Infomation Details"):
        total_students_block = df_selected_block.count().sum()
        average_score_block = np.mean(df_selected_block)
        most_common_score_block = round(df_selected_block.mode().iloc[0], 2)

        st.write(f"Total number of students: {total_students_block:,}")
        st.write(f"Average score: {average_score_block:.2f}")
        st.write(f"Most common score achieved by students: {most_common_score_block:.2f}")
