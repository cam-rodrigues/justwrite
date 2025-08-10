import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Just Write",
    layout="wide"
)

# --- Sidebar ---
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "Drafts", "Editing Tools", "Export & Share"]
)

# --- Page Content ---
if page == "Home":
    st.title("Just Write")
    st.write("Welcome to your personal writing workspace. More tools will appear here once they’re ready.")

elif page == "Drafts":
    st.title("Drafts")
    st.write("Create and edit your writing projects.")

elif page == "Editing Tools":
    st.title("Editing Tools")
    st.write("Access grammar checks, style improvements, and more.")

elif page == "Export & Share":
    st.title("Export & Share")
    st.write("Export your work to Word, PDF, or Google Docs.")

# --- Footer ---
st.markdown("---")
st.caption("Just Write — Your all-in-one writing assistant.")
