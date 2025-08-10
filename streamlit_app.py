import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Just Write",
    layout="centered"
)

# --- Main Layout ---
st.title("Just Write")
st.write("Welcome to your personal writing workspace. More tools will appear here once they’re ready.")

# Placeholder sections
st.header("Drafts")
st.write("Create and edit your writing projects.")

st.header("Editing Tools")
st.write("Access grammar checks, style improvements, and more.")

st.header("Export & Share")
st.write("Export your work to Word, PDF, or Google Docs.")

# Footer
st.markdown("---")
st.caption("Just Write — Your all-in-one writing assistant.")
