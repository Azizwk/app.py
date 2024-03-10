import streamlit as st
import pandas as pd
import numpy as np


# Create some sample data
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Define the layout
st.title('My Streamlit Dashboard')
st.write('Here is some sample data:')
st.write(data)

# Create a scatter plot using Plotly Express
fig = px.scatter(data, x='x', y='y', title='Scatter Plot')
st.plotly_chart(fig)
