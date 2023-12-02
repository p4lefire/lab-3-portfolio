import streamlit as st
import info 
import pandas as pd

#About Me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width=400)
    st.write(info.about_me)
    st.write('---')
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Check out my GitHub\n(work in progress)")
    github_link=f'<a href="{info.my_github_url}"> <img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html=f'<a href="mailto:{info.my_email_address}"> <img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True
        )
    st.write("---")

education_section(info.education_data, info.course_data)

#Professional Experience

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)

#Projects
def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")

project_section(info.projects_data)

#Skills

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill} {info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, profiency in spoken_data.items():
        st.write(f"{spoken} {info.spoken_icons.get(spoken, '')}: {profiency}")
    
    st.write("---")

skills_section(info.programming_data, info.spoken_data)

#Activities

def activities_section(hs_data, college_data):
    st.header("Extracurriculars")
    tab1, tab2 = st.tabs(["High School", "College"])
    with tab1:
        st.subheader("High School")
        for title, (details, image) in hs_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("College")
        for title, details in college_data.items():
            expander = st.expander(f"{title}")
            for bullets in details:
                expander.write(bullets)
    st.write("---")

activities_section(info.hs_data, info.college_data)  