import streamlit as st

# 1. PAGE ARCHITECTURE
st.set_page_config(page_title="Aggarwal Store | Premium Delivery", layout="wide", page_icon="🛍️")

# 2. THE DESIGN ENGINE (CSS)
# This block transforms Streamlit into a polished mobile-first UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    /* Main App Container */
    .stApp {
        background-color: #FBFBFB;
    }

    /* Premium Header */
    .header-container {
        background: #F7D106;
        padding: 30px 20px;
        border-radius: 0 0 30px 30px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0 10px 30px rgba(247, 209, 6, 0.2);
    }
    .brand-title {
        font-size: 32px;
        font-weight: 900;
        color: #000;
        margin-bottom: 5px;
        letter-spacing: -1.5px;
    }
    .location-badge {
        background: rgba(0,0,0,0.05);
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 700;
    }

    /* Search Bar Customization */
    div[data-baseweb="input"] {
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    }

    /* Modern Product Card */
    .product-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        border: 1px solid #F0F0F0;
        transition: all 0.3s ease;
    }
    .product-card:hover {
        border-color: #F7D106;
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    }

    /* Aesthetic Pricing */
    .price-container {
        margin: 15px 0;
    }
    .current-price {
        font-size: 20px;
        font-weight: 800;
        color: #000;
    }
    .old-price {
        text-decoration: line-through;
        color: #999;
        font-size: 14px;
        margin-left: 8px;
    }

    /* Add Button - Blinkit Green */
    .stButton>button {
        background-color: #0C831F !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 25px !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #096317 !important;
        box-shadow: 0 4px 15px rgba(12, 131, 31, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. CONTENT SECTIONS

# A. Header & Brand
st.markdown("""
    <div class="header-container">
        <div class="brand-title">AGGARWAL STORE</div>
        <span class="location-badge">📍 Delivering to Phase 3, Gurgaon • 8 Mins</span>
    </div>
""", unsafe_allow_html=True)

# B. Search & Promotion
col_s1, col_s2, col_s3 = st.columns([1, 4, 1])
with col_s2:
    st.text_input("Search", placeholder="Search 'Milk', 'Snacks', or 'Beverages'...", label_visibility="collapsed")
    st.image("https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80&w=1000", 
             caption="Quality Assured Groceries", use_container_width=True)

# C. Product Display
st.markdown("### ⚡ Trending in Gurgaon")

# Reliable Product Database
products = [
    {
        "name": "Haldiram's Bhujia Sev",
        "weight": "400g",
        "price": 99,
        "mrp": 110,
        "img": "https://m.media-amazon.com/images/I/81vJ9S-Z7VL._SL1500_.jpg",
        "tag": "Best Seller"
    },
    {
        "name": "Thums Up (Chilled)",
        "weight": "750ml",
        "price": 40,
        "mrp": 45,
        "img": "https://m.media-amazon.com/images/I/610C86pY6DL._SL1500_.jpg",
        "tag": "11% OFF"
    },
    {
        "name": "Britannia Good Day",
        "weight": "600g",
        "price": 120,
        "mrp": 140,
        "img": "https://m.media-amazon.com/images/I/71YvYl-f-aL._SL1500_.jpg",
        "tag": "Super Saver"
    },
    {
        "name": "Amul Fresh Milk",
        "weight": "1L",
        "price": 66,
        "mrp": 68,
        "img": "https://m.media-amazon.com/images/I/51-u0B-O3vL._SL1000_.jpg",
        "tag": "Daily Essential"
    }
]

# 2-Column Responsive Grid
cols = st.columns(2)
for i, p in enumerate(products):
    with cols[i % 2]:
        st.markdown(f"""
            <div class="product-card">
                <div style="text-align: left;"><span style="background: #2563eb; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;">{p['tag']}</span></div>
                <img src="{p['img']}" style="width: 100%; height: 140px; object-fit: contain; margin-top: 10px;">
                <p style="margin: 10px 0 0 0; font-weight: 700; font-size: 16px;">{p['name']}</p>
                <p style="color: #666; font-size: 12px; margin: 0;">{p['weight']}</p>
                <div class="price-container">
                    <span class="current-price">₹{p['price']}</span>
                    <span class="old-price">₹{p['mrp']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("ADD", key=f"add_{i}")

# D. Floating Bottom Bar (Front-end only representation)
st.markdown("""
    <div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); width: 90%; max-width: 400px; background: #000; color: white; padding: 15px 25px; border-radius: 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 1000;">
        <div style="font-weight: 700;">2 ITEMS • ₹139</div>
        <div style="color: #F7D106; font-weight: 900; cursor: pointer;">VIEW CART 🛒</div>
    </div>
""", unsafe_allow_html=True)
