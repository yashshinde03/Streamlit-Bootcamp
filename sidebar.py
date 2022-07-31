import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')

data = {
    "num": [x for x in range(1, 11)],
    "square": [x ** 2 for x in range(1, 11)],
    "twice": [x * 2 for x in range(1, 11)],
    "thrice": [x * 3 for x in range(1, 11)]
}

df = pd.DataFrame(data=data)

# st.sidebar.selectbox("Select a number",[1,2,3,4,5])
# col = st.sidebar.selectbox("Select a column", df.columns)

# plt.plot(df['num'], df[col])

# st.pyplot()

col = st.sidebar.multiselect("Select a column", df.columns)

plt.plot(df['num'], df[col])

st.pyplot()