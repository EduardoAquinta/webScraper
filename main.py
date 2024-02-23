import requests
from bs4 import BeautifulSoup
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="DCMS Data Pool",
    page_icon="\U0001F600"
)
st.sidebar.success("Welcome to the DCMS Data Pool.")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


with st.form("Ingest"):
    st.header("Enter the URL you would like to ingest: ")
    user_url = st.text_input("Enter the url")
    st.form_submit_button("Ingest", on_click=click_button)

add_vertical_space(3)
st.text("useful urls:")
st.text('https://www.ons.gov.uk/peoplepopulationandcommunity/leisureandtourism#datasets')
add_vertical_space(3)


def web_lookup():
    url = user_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('ul', {'class': 'list--neutral margin-top--half'})
    ons_datasets = results.find_all("a", {'class': 'underline-link'})

    for element in ons_datasets:
        st.write(element.text.strip())



if st.session_state.clicked:
    st.write(web_lookup())

# "https://realpython.github.io/fake-jobs/"
