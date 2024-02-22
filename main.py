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

st.text("useful urls:")
st.text('https://www.ons.gov.uk/peoplepopulationandcommunity/leisureandtourism#datasets')


def web_lookup():
    url = user_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('ul', {'class': 'list--neutral margin-top--half'})
    ons_datasets = results.find_all("a", {'class': 'underline-link'})

    for element in ons_datasets:
        st.text(element.text.strip())
        st.text("-----")


if st.session_state.clicked:
    st.write(web_lookup())

# "https://realpython.github.io/fake-jobs/"
