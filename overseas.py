import pandas as pd
import streamlit as st
import numpy as np

st.title("Overseas Visitors to the UK")
url = ("https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/leisureandtourism/datasets"
       "/monthlyoverseastravelandtourismreferencetables/current/referencetables2023q3.xlsx")

DATE_COLUMN = 'date/time'
DATA_URL = url


@st.cache_data
def load_data(nrows):
    data = pd.read_excel(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')

data = load_data(10000)

data_load_state.text('Loading data... done!')
