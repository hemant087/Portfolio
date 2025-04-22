import streamlit as st

# Set page title
st.set_page_config(page_title="Hemant Raj's Portfolio", page_icon=":guardsman:", layout="wide")

# Header Section
st.title("Hemant Raj's Portfolio")
st.write("Welcome to my personal portfolio website! I'm a Data Scientist, Python Developer, and Robotics Enthusiast.")

# About Me Section
st.header("About Me")
st.write("""
    Hi, I'm Hemant Raj. I am passionate about programming, data science, machine learning, and robotics. 
    I have experience working with Python, machine learning algorithms, deep learning frameworks, 
    and a variety of other tools to develop intelligent systems and automation projects.
""")

# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages:** Python, C/C++, LaTeX, MarkDown, PHP
- **Data Science Tools:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook
- **Machine Learning:** Supervised & Unsupervised Learning, Logistic Regression, K-Means Clustering
- **Deep Learning:** ANN, CNN, TensorFlow, PyTorch
- **Other Tools:** MySQL, Django, FastAPI, Excel, Canva
- **Concepts:** Statistics, Probability, Linear Algebra, Calculus, Data Preprocessing, EDA
""")

# Projects Section
st.header("Projects")
st.write("Here are some of the projects I've worked on:")

# Project 1
st.subheader("1. CCTV Based Auto Attendance System")
st.write("""
    A project where I used Raspberry Pi and camera modules for automatic attendance tracking using face recognition. 
    It employs the LBPH (Local Binary Patterns Histograms) algorithm for accurate recognition.
    [GitHub Repo](https://github.com/hemant087) for the code and further details.
""")

# Project 2
st.subheader("2. AI-based School Attendance System")
st.write("""
    A web-based system built using the MERN stack, implementing AI for attendance tracking and analytics. 
    The system includes feedback collection and an analytics dashboard.
""")

# Contact Section
st.header("Contact Me")
st.write("""
Feel free to reach out for collaborations or inquiries:
- **Email:** hemantraj587@gmail.com
- **LinkedIn:** [Hemant Raj's LinkedIn](https://www.linkedin.com/in/hemant-raj087)
- **GitHub:** [Hemant Raj's GitHub](https://github.com/hemant087)
""")

# Footer
st.write("---")
st.write("Created with ❤️ by Hemant Raj.")
