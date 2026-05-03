import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Aggarwal Store | Gurgaon", layout="centered", page_icon="🏪")

# 2. BRANDING & UI/UX CSS
st.markdown("""
<style>
    /* Main Banner Branding */
    .brand-banner {
        background-color: #F7D106;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: black;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .brand-name {
        font-size: 28px;
        font-weight: 900;
        margin: 0;
        letter-spacing: -1px;
    }
    .delivery-tag {
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
    }
    /* Product Card */
    .product-card {
        background: white;
        padding: 10px;
        border-radius: 12px;
        border: 1px solid #f0f0f0;
        margin-bottom: 20px;
    }
    /* Add Button */
    .stButton>button {
        background-color: #0c831f !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 3. STABLE PRODUCT DATA (Using Wikimedia/Open links to ensure visibility)
products = [
    {
        "name": "Traditional Bhujia",
        "price": 99, "mrp": 110, "off": "10% OFF",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Bikaneri_Bhujia.jpg/640px-Bikaneri_Bhujia.jpg"
    },
    {
        "name": "Cold Cola (Glass)",
        "price": 40, "mrp": 45, "off": "11% OFF",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Glass_of_Cola.jpg/640px-Glass_of_Cola.jpg"
    },
    {
        "name": "Butter Cookies",
        "price": 120, "mrp": 140, "off": "14% OFF",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Danish_Butter_Cookies.jpg/640px-Danish_Butter_Cookies.jpg"
    }
]

# 4. TOP NAVIGATION & BANNER
st.markdown("""
    <div class="brand-banner">
        <p class="brand-name">AGGARWAL STORE</p>
        <p class="delivery-tag">⚡ 10 Min Delivery to Phase 3</p>
    </div>
""", unsafe_allow_html=True)

st.text_input("Search groceries...", placeholder="Search 'Cold Drink'", label_visibility="collapsed")

# 5. DYNAMIC PRODUCT GRID
st.write("### Trending Today")
cols = st.columns(2)

for idx, p in enumerate(products):
    with cols[idx % 2]:
        # Using a container to group elements visually
        with st.container():
            st.markdown(f'<span style="background:#2563eb; color:white; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;">{p["off"]}</span>', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**")
            st.markdown(f"**₹{p['price']}** <span style='color:gray; text-decoration:line-through; font-size:12px;'>₹{p['mrp']}</span>", unsafe_allow_html=True)
            st.button("ADD", key=f"add_{idx}")

# 6. FLOATING CHECKOUT ACTION
st.divider()
st.button("🛒 View Cart & Checkout", use_container_width=True, type="primary")
