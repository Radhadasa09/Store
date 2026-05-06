import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# ── 1. Page Config (Must be first) ──────────────────────────────────────────
st.set_page_config(
    page_title="Digital Dukaan | Aggarwal Store",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()

# Try to load custom CSS, fallback if not found
try:
    from components.ui import inject_global_css
    inject_global_css()
except ModuleNotFoundError:
    # Fallback CSS if components/ui.py is missing
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
            html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
            #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
            [data-testid="stSidebar"] { background-color: #0F172A; color: white;}
            .stButton>button { background-color: #0C831F !important; color: white !important; font-weight: bold; width: 100%; border-radius: 8px;}
        </style>
    """, unsafe_allow_html=True)

# ── 2. Mock Database for Presentation ───────────────────────────────────────
# In production, this will be replaced by a Supabase database query.
MOCK_INVENTORY = {
    "milk": {"mrp": 68, "price": 66},
    "bread": {"mrp": 50, "price": 45},
    "bhujia": {"mrp": 110, "price": 99},
    "thums up": {"mrp": 45, "price": 40},
    "eggs": {"mrp": 80, "price": 75},
    "sugar": {"mrp": 55, "price": 50},
    "rice": {"mrp": 150, "price": 135},
    "default": {"mrp": 100, "price": 90} # For unknown items
}

def smart_price_lookup(item_name):
    """Matches typed items to inventory to auto-fetch prices."""
    clean_name = item_name.lower().strip()
    for key in MOCK_INVENTORY:
        if key in clean_name:
            return MOCK_INVENTORY[key]
    return MOCK_INVENTORY["default"]

# ── 3. Mode Routing ─────────────────────────────────────────────────────────
params = st.query_params
mode = params.get("mode", "owner")

if mode == "customer":
    # 🛒 CUSTOMER STOREFRONT: Smart List UI
    st.markdown("<h1 style='text-align: center; color: #F7D106;'>⚡ Aggarwal Store</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Smart Order List | 10 Min Delivery</p>", unsafe_allow_html=True)
    
    st.info("📝 Type what you need below. Our system will auto-calculate your final bill with store discounts.")
    
    raw_list = st.text_area("Your Shopping List (One item per line):", height=150, 
                            placeholder="e.g.\nAmul Milk 1L\nBrown Bread\nHaldiram Bhujia")
    
    if st.button("Calculate Final Bill"):
        if raw_list:
            items = [item.strip() for item in raw_list.split('\n') if item.strip()]
            
            bill_data = []
            total_mrp = 0
            total_price = 0
            
            for item in items:
                pricing = smart_price_lookup(item)
                bill_data.append({
                    "Item": item.title(),
                    "MRP (₹)": pricing["mrp"],
                    "Our Price (₹)": pricing["price"]
                })
                total_mrp += pricing["mrp"]
                total_price += pricing["price"]
            
            savings = total_mrp - total_price
            
            # Display Results
            st.divider()
            st.subheader("🧾 Your Instant Bill")
            
            # Metrics Row
            m1, m2, m3 = st.columns(3)
            m1.metric("Total MRP", f"₹{total_mrp}")
            m2.metric("Total to Pay", f"₹{total_price}")
            m3.metric("Your Savings", f"₹{savings}", f"{int((savings/total_mrp)*100)}% Off")
            
            # Detailed Bill Table
            df = pd.DataFrame(bill_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            st.success("✅ Ready to order! Your neighborhood store will pack this instantly.")
            
            # Place Order Button representation
            st.markdown("""
                <div style="background: black; color: white; padding: 15px; border-radius: 10px; text-align: center; margin-top: 15px; font-weight: bold; cursor: pointer;">
                    CONFIRM ORDER & PAY ₹{} ON DELIVERY
                </div>
            """.format(total_price), unsafe_allow_html=True)
        else:
            st.warning("Please type at least one item to calculate the bill.")

    # Sidebar switch for presentation
    with st.sidebar:
        st.markdown("### Customer View Active")
        if st.button("Switch to Owner Dashboard"):
            st.query_params.clear()
            st.rerun()

else:
    # 📊 OWNER DASHBOARD
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;">
          <span style="font-size:2.5rem">🏪</span>
          <h2 style="font-family:'Baloo 2',cursive; color:#F8FAFC; margin:0;">Digital Dukaan</h2>
          <p style="color:#94A3B8; font-size:0.8rem; margin:0;">Owner Dashboard</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

        page = st.radio(
            "Navigation",
            options=["📊 Dashboard", "📦 Live Orders", "📒 Khata Ledger", "💰 Platform Wallet"],
            label_visibility="collapsed"
        )
        
        st.divider()
        if st.button("🛒 View Smart Storefront"):
            st.query_params.update(mode="customer")
            st.rerun()

    # Dashboard Logic
    st.title(page)
    
    if page == "📊 Dashboard":
        m1, m2, m3 = st.columns(3)
        m1.metric("Today's Orders", "14", "+3")
        m2.metric("Total Khata Credit", "₹8,450")
        m3.metric("Platform Wallet", "₹920", "-₹24", delta_color="inverse")
        
        st.subheader("Incoming 'Smart List' Orders")
        st.table([
            {"Time": "10:45 AM", "Customer": "Sector 3, House 42", "Items": "Milk, Bread, Eggs", "Value": "₹186", "Status": "Pending"},
            {"Time": "09:30 AM", "Customer": "Sector 3, House 12", "Items": "Bhujia, Thums Up", "Value": "₹139", "Status": "Delivered"}
        ])
        
    elif page == "💰 Platform Wallet":
        st.warning("Current Wallet Balance: ₹920. Auto-deductions active for new orders (3% fee).")
        st.progress(920/2000)
