import requests
from bs4 import BeautifulSoup
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="DCMS Data Automation",
    page_icon="\U0001F600"
)

with st.sidebar:
    st.image("./images/DCMS-logo.png")
    st.success("Welcome to the DCMS Data Ingestion Automation Tool.")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


with st.form("Ingest"):
    st.header("Enter the URL you would like to start automating: ", divider="red")
    user_url = st.text_input("Enter the url here:")
    st.form_submit_button("Ingest", on_click=click_button)

add_vertical_space(3)
st.text("useful urls:")
st.text('https://www.ons.gov.uk/peoplepopulationandcommunity/leisureandtourism#datasets')
add_vertical_space(3)
st.text("List of potential data resources:")


def web_lookup():
    url = user_url
    url_no_hashtag = user_url.replace("/peoplepopulationandcommunity/leisureandtourism#datasets", "")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('ul', {'class': 'list--neutral margin-top--half'})
    links = []
    for link in results.find_all('a'):
        if link.has_attr('href'):
            href = link['href']
            if href and not href.startswith('#'):
                links.append(href)
    for element in links:
        st.write(url_no_hashtag + element)


if st.session_state.clicked:
    st.write(web_lookup())

# "https://realpython.github.io/fake-jobs/"
