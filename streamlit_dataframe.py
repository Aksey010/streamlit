import streamlit as st
import numpy as np
import pandas as pd


arr = np.random.normal(1, 1, size=100)

options = st.sidebar.multiselect(
    'Как фильтровать значения?',
    ['>0', '<0', 'All'],
    ['All']
)

try:
    if options[0] == 'All':
        mask = arr == arr
    elif options[0] == '>0':
        mask = arr > 0
    else:
        mask = arr < 0

    df = pd.DataFrame(arr[mask])
except:
    df = pd.DataFrame(arr)

st.write(df)
