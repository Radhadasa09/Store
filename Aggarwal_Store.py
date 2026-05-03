import streamlit as st
from dotenv import load_dotenv

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Digital Dukaan | Aggarwal Store",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load environment variables for Supabase/API keys
load_dotenv()

# --- Internal Component: Global CSS ---
def inject_global_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Baloo+2:wght@600;800&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        
        /* Sidebar Styling for Owner Mode */
        [data-testid="stSidebar"] { background-color: #0F172A; color: #F8FAFC; }
        
        /* Blinkit Green Buttons */
        .stButton>button {
            background-color: #0C831F !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

inject_global_css()

# --- Mode Detection Logic ---
# Checks for ?mode=customer in the URL
params = st.query_params
mode = params.get("mode", "owner")

if mode == "customer":
    # 🛒 CUSTOMER STOREFRONT
    st.markdown("<h1 style='text-align: center; color: #F7D106;'>⚡ Aggarwal Store</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Delivering to Phase 3, Gurgaon in 10 Mins</p>", unsafe_allow_html=True)
    
    # Simple Storefront Preview
    cols = st.columns(2)
    products = [
        {"name": "Haldiram's Bhujia", "price": "₹99", "img": "https://placehold.co/200x200?text=Bhujia"},
        {"name": "Amul Milk (1L)", "price": "₹66", "img": "https://placehold.co/200x200?text=Milk"}
    ]
    
    for idx, p in enumerate(products):
        with cols[idx % 2]:
            st.image(p["img"])
            st.write(f"**{p['name']}**")
            st.write(p["price"])
            st.button("ADD", key=f"cust_{idx}")
            
    st.sidebar.info("Logged in as Customer")
    if st.sidebar.button("Switch to Owner View"):
        st.query_params.clear()
        st.rerun()

else:
    # 📊 OWNER DASHBOARD
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;">
          <span style="font-size:2.5rem">🏪</span>
          <h2 style="font-family:'Baloo 2',cursive; color:#F8FAFC;">Digital Dukaan</h2>
          <p style="color:#94A3B8; font-size:0.8rem;">Owner Dashboard</p>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "Navigation",
            options=["📊 Dashboard", "📦 Orders", "📒 Khata Ledger", "💰 Wallet"],
            label_visibility="collapsed"
        )
        
        st.divider()
        if st.button("🛒 View Storefront"):
            st.query_params.update(mode="customer")
            st.rerun()

    # Dashboard Logic
    if page == "📊 Dashboard":
        st.title("Business Overview")
        m1, m2, m3 = st.columns(3)
        m1.metric("Today's Orders", "24", "+15%")
        m2.metric("Khata Balance", "₹12,450", "Pending")
        m3.metric("Platform Wallet", "₹840", "-₹60", delta_color="inverse")
        
        st.subheader("Recent Activity")
        st.table([
            {"Type": "Delivery", "Value": "₹450", "Comm (3%)": "₹13.5"},
            {"Type": "Khata Pay", "Value": "₹1,000", "Comm (1%)": "₹10.0"}
        ])

    elif page == "💰 Wallet":
        st.title("Wallet & Billing")
        st.warning("Wallet Balance: ₹840. Auto-deductions active.")
        st.progress(840/2000) # Assuming 2000 is top-up target
