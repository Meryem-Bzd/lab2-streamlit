import streamlit as st
from utils import search_producthunt

st.title("🔍 Search Results")

search_term = st.text_input("Enter your search term:")

if search_term:
    with st.spinner("Searching..."):
        df = search_producthunt(search_term)
        if not df.empty:
            st.success("Results found!")
            st.dataframe(df)
            # Save to session state
            st.session_state["results_df"] = df
        else:
            st.warning("No results found.")
