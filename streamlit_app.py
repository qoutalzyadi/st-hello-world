#Import all relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import dtale
import sweetviz as sv

## This statement allows the visuals to render within your Jupyter Notebook.
%matplotlib inline

import streamlit as st
st.subheader("Hi , I'm Qout")
st.title("Analysis of Job Advertisements in the Kingdom")
st.write("Hello, I work as a Recruitment Officer at a volunteer organization dedicated to employing and developing young people in the Kingdom. Recently, I have been tasked with analyzing job advertisements to understand the labor market needs and employment trends for young job seekers.")
st.write("I started collecting job data from various sources, including online recruitment and local newspapers. I reviewed the data to understand the distribution of jobs by region, sector, and experience requirements.")

st.image("")

st.write("Based on the analyzed data, it was found that 403 job advertisements specifically sought women, 480 job advertisements sought men, and 586 job advertisements did not specify a particular gender.")
st.write("It appears that there is a varying distribution of job advertisements across different regions, which can provide an initial insight into where the primary job concentrations are in the Kingdom.")
st.write("After reviewing the data, it appears that the highest demand in job advertisements is for individuals with no prior experience. This indicates that there is an active job market targeting recent graduates and those seeking opportunities to develop their skills and build their initial career paths.")
