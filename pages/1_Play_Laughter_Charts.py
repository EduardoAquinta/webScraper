import pandas as pd
import streamlit as st
import numpy as np

st.title("Playscheme data-sphere")
url = 'data.csv'

DATE_COLUMN = 'date'
AMOUNT_COLUMN = 'amount'
NAME_COLUMN = 'name'
DATA_URL = url


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')

data = load_data(10)

data_load_state.text('Loading data... done!')

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

st.subheader('Laughs per Hour')

progress_bar = st.progress(0)
status_text = st.sidebar.empty()
st.line_chart(data, x=NAME_COLUMN, y=AMOUNT_COLUMN)
