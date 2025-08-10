import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Just Write",
    layout="centered"
)

# --- Main Layout ---
st.title("Just Write")
st.write("This is your personal writing workspace. More tools coming soon!")

# Placeholder sections for future pages
st.header("Drafts")
st.write("Here you’ll be able to create and edit your writing projects.")

st.header("Editing Tools")
st.write("Here you’ll have grammar checks, style improvements, and more.")

st.header("Export & Share")
st.write("Here you’ll export your work to Word, PDF, or Google Docs.")

# Footer
st.markdown("---")
st.caption("Just Write — Your all-in-one writing assistant.")
