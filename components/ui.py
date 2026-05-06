import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
        /* 1. Import Premium Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Baloo+2:wght@600;800&display=swap');
        
        /* 2. Set Global Font */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* 3. Hide Streamlit Branding (for a professional look) */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* 4. Custom Sidebar Styling for Owner Mode */
        [data-testid="stSidebar"] {
            background-color: #0F172A; /* Deep Navy */
        }
    </style>
    """, unsafe_allow_html=True)
