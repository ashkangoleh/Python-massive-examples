import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2
x1 = np.random.randn(500) - 2
x2 = np.random.randn(1000)
x3 = np.random.randn(750) + 2
# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Transaction', 'Inputs', 'Outputs']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.500, .1000, .750])

# Plot!
st.plotly_chart(fig, use_container_width=True)