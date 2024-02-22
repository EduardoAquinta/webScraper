import requests
from bs4 import BeautifulSoup
import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


with st.form("Ingest"):
    st.header("Enter the URL you would like to ingest: ")
    user_url = st.text_input("Enter the url")
    st.form_submit_button("Ingest", on_click=click_button)


def web_lookup():
    url = user_url
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job_element in python_job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        st.text(title_element.text.strip())
        st.text(company_element.text.strip())
        st.text(location_element.text.strip())
        st.text("-----")


if st.session_state.clicked:
    st.write(web_lookup())

# "https://realpython.github.io/fake-jobs/"
