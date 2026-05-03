import streamlit as st

# 1. PAGE ARCHITECTURE
st.set_page_config(page_title="Aggarwal Store | Gurgaon", layout="centered", page_icon="🏪")

# 2. THE DESIGN ENGINE (CSS)
# Focus: High-contrast, clean lines, and mobile-ready components
st.markdown("""
<style>
    /* Premium Header */
    .brand-header {
        background-color: #F7D106;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: black;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .brand-name {
        font-size: 32px;
        font-weight: 900;
        margin: 0;
        letter-spacing: -1px;
    }
    .delivery-tag {
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        background: rgba(0,0,0,0.08);
        padding: 4px 12px;
        border-radius: 50px;
        display: inline-block;
        margin-top: 10px;
    }
    
    /* Symbol-Based Card */
    .symbol-card {
        background: white;
        border: 1px solid #eee;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
    }

    /* Professional Pricing */
    .price-box {
        margin: 10px 0;
        font-size: 18px;
        font-weight: 800;
    }
    .mrp-text {
        text-decoration: line-through;
        color: #999;
        font-size: 13px;
        font-weight: 400;
    }

    /* Blinkit Green Button */
    .stButton>button {
        background-color: #0c831f !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 700 !important;
        width: 100%;
        height: 45px;
    }
</style>
""", unsafe_allow_html=True)

# 3. SYMBOL-BASED CATALOG
# Using placeholder symbols with clear labels to ensure zero image failures
catalog = [
    {
        "name": "Haldiram's Bhujia", "spec": "400g", "price": 99, "mrp": 110, "tag": "BESTSELLER",
        "symbol": "https://placehold.co/400x400/FFF9C4/000000?text=SNACK"
    },
    {
        "name": "Thums Up (Chilled)", "spec": "750ml", "price": 40, "mrp": 45, "tag": "CHILLED",
        "symbol": "https://placehold.co/400x400/E3F2FD/000000?text=DRINK"
    },
    {
        "name": "Britannia Biscuits", "spec": "600g", "price": 120, "mrp": 140, "tag": "14% OFF",
        "symbol": "https://placehold.co/400x400/FCE4EC/000000?text=SWEET"
    },
    {
        "name": "Amul Taaza Milk", "spec": "1L", "price": 66, "mrp": 68, "tag": "FRESH",
        "symbol": "https://placehold.co/400x400/E8F5E9/000000?text=DAIRY"
    }
]

# 4. TOP NAVIGATION
st.markdown("""
    <div class="brand-header">
        <p class="brand-name">AGGARWAL STORE</p>
        <p class="delivery-tag">⚡ 10 MIN DELIVERY TO PHASE 3, GURGAON</p>
    </div>
""", unsafe_allow_html=True)

st.text_input("", placeholder="Search 'Milk', 'Bread' or 'Biscuits'...", label_visibility="collapsed")

# 5. DYNAMIC GRID (2 COLUMNS)
st.write("### Trending Today")
cols = st.columns(2)

for idx, item in enumerate(catalog):
    with cols[idx % 2]:
        # Card Layout
        with st.container():
            st.markdown(f'<span style="background:#2563eb; color:white; padding:2px 8px; border-radius:4px; font-size:10px; font-weight:bold;">{item["tag"]}</span>', unsafe_allow_html=True)
            st.image(item["symbol"], use_container_width=True)
            st.write(f"**{item['name']}**")
            st.caption(item["spec"])
            st.markdown(f'<div class="price-box">₹{item["price"]} <span class="mrp-text">₹{item["mrp"]}</span></div>', unsafe_allow_html=True)
            st.button("ADD", key=f"add_{idx}")

# 6. FIXED BOTTOM CHECKOUT (Representation)
st.divider()
st.markdown("""
    <div style="background: black; color: white; padding: 15px; border-radius: 15px; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-weight: 700;">🛒 2 ITEMS • ₹139</div>
        <div style="color: #F7D106; font-weight: 900;">VIEW CART</div>
    </div>
""", unsafe_allow_html=True)
