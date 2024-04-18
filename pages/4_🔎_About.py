
import streamlit as st
import requests
import PIL.Image as Image


def new_line():
    st.markdown("<br>", unsafe_allow_html=True)


# Define a function to load the Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Config
page_icon = Image.open("./assets/icon.png")
st.set_page_config(layout="centered", page_title="Click ML", page_icon=page_icon)


# Create the About page
def main():
    # Title Page
    st.markdown("<h1 align='center'> 🔎About", unsafe_allow_html=True)
    new_line()

    # What is ClickML?
    st.markdown("Welcome to ClickML, an intuitive and powerful machine learning application designed to simplify the process of building and evaluating machine learning models. Whether you're a beginner or an experienced data scientist, ClickML provides a user-friendly interface to streamline your machine learning workflows.", unsafe_allow_html=True)
    st.markdown("It is no-code easy-to-use platfrom which allows you to build machine learning models without writing a single line of code. \n ")
    
    
    # what this app does with the main, quickml, and study_time pages
    st.markdown("This app is divided into three main tabs: **👉 ClickML**, **🚀 QuickML**, and **📚 StudyML**.", unsafe_allow_html=True)
    st.write("\n")

    # ClickML
    st.markdown("### 👉 ClickML")
    st.markdown("- **ClickML:** This section is the main page of the **ClickML** web app. It provides the customizability to build Machine Learning models by selecting and applying the Data Preparation techniques that fits your data. Also, you can try differnet Machine Learning models and tune the hyperparameters to get the best model.", unsafe_allow_html=True)
    st.write("\n")

    # QuickML
    st.markdown("### 🚀 QuickML")
    st.markdown("- **QuickML:** QuickML is a tab that allows you to build a model quickly with just a few clicks. This tab is designed for people who are new to Machine Learning and want to build a model quickly without having to go through the entire process of Exploratory Data Analysis, Data Cleaning, Feature Engineering, etc. It is just a quick way to build a model for testing purposes.", unsafe_allow_html=True)
    st.write("\n")

    # StudyML
    st.markdown("### 📚 StudyML")
    st.markdown("- **Study Time:** The StudyML tab is designed to help you to understand the key concepts of building machine learning models. This tab has 7 sections, each section talk about a specific concept in building machine learning models. With each section you will have the uplility to apply the concepts of this sections on multiple datasets. The code the Explaination and everything you need to understand is in this tab.", unsafe_allow_html=True)
    new_line()

    # Why ClickML?
    st.header("✨ Why Choose ClickML?")
    st.markdown("""
- **User-Friendly Interface**: ClickML offers an intuitive and easy-to-use interface, making machine learning accessible to users of all skill levels.
- **Efficiency and Speed**: With ClickML, you can quickly build, train, and evaluate machine learning models, reducing the time and effort required.
- **Comprehensive Learning Resources**: The StudyML tab provides detailed explanations, code examples, and visualizations to enhance your understanding of machine learning concepts.
- **Flexible and Customizable**: ClickML supports a wide range of algorithms and allows you to fine-tune model parameters to meet your specific requirements.

                """, unsafe_allow_html=True)
    new_line()

                

if __name__ == "__main__":
    main()
