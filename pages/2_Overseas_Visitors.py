import pandas as pd
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.title("Overseas Visitors to UK Q3 2023")
url = 'referencetables2023q3.xlsx'

DATE_COLUMN = 'Period'
AMOUNT_COLUMN = 'Seasonally Adjusted World Total'
NAME_COLUMN = 'name'
DATA_URL = url


@st.cache_data
def load_data(nrows):
    data = pd.read_excel(DATA_URL, sheet_name="1", nrows=nrows, header=None)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.columns = data.iloc[3]
    return data.tail(-4)


data_load_state = st.text('Loading data...')

data = load_data(14)

data_load_state.text('Loading data... done!')

if st.checkbox('Show Raw Data'):
    st.subheader('First 10 entries from the raw data')
    st.write(data)
add_vertical_space(3)
st.subheader('Uk Overseas Visitors per month')
add_vertical_space(1)

progress_bar = st.progress(0)
status_text = st.sidebar.empty()
st.line_chart(data, x=DATE_COLUMN, y=AMOUNT_COLUMN)
