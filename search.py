import sys
lines = open('app.py', encoding='utf-8').readlines()
with open('search.txt', 'w', encoding='utf-8') as f:
    for i, ln in enumerate(lines):
        ln_lower = ln.lower()
        if 'research' in ln_lower or 'ashrae' in ln_lower:
            f.write(f'{i+1}: {ln}')

import streamlit as st

st.set_page_config(page_title="Energy Model", layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("Menu")

page = st.sidebar.radio("Navigation", ["Home", "Dashboard", "Model"])

if page == "Home":
    st.title("Home Page")

elif page == "Dashboard":
    st.title("Dashboard")

elif page == "Model":
    st.title("Energy Model")