import streamlit as st

st.write('Hello world!')

dashboard = st.Page("./page/dashboard.py", title="Dashboard")
nabung = st.Page("./page/nabung.py", title="Nabung")

pg= st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []

pg.run()