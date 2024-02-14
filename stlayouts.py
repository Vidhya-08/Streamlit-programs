import streamlit as st
add=st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email","Home Phone","Mobile Phone"))

with st.sidebar:
    add_radio=st.radio(
        "Choose a shipping method",
        ("Standard Shipping","Premium Shipping"))

    
c1,c2,c3=st.columns(3)
with c1:
    st.header("This is column 1")
    st.write("Some text inside column 1")

with c2:
    st.header("This is column 2")
    st.write("Some text inside column 2")

with c3:
    st.header("This is column 3")
    st.write("Some text inside column 3")


st.title("Expander")
with st.expander("Expand me to see some text"):
    st.write("Expanded")
    
