import streamlit as st

# 1. Page Config
st.set_page_config(layout="centered", page_title="Blinkit | Phase 3 Delivery")

# 2. Custom Branding CSS
st.markdown("""
<style>
    .header-box {
        background-color: #F7D106;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        color: black;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #0c831f !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
        font-weight: bold;
    }
    .discount-badge {
        background-color: #2563eb;
        color: white;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 11px;
        position: absolute;
        z-index: 10;
    }
</style>
""", unsafe_allow_html=True)

# 3. Product Catalog
catalog = [
    {
        "name": "Haldiram's Bhujia Sev (400g)",
        "price": 99, "mrp": 110, "off": "10% OFF",
        "url": "https://m.media-amazon.com/images/I/81vJ9S-Z7VL._SL1500_.jpg"
    },
    {
        "name": "Thums Up (750ml) - Chilled",
        "price": 40, "mrp": 45, "off": "11% OFF",
        "url": "https://m.media-amazon.com/images/I/610C86pY6DL._SL1500_.jpg"
    },
    {
        "name": "Britannia Good Day Biscuits",
        "price": 120, "mrp": 140, "off": "14% OFF",
        "url": "https://m.media-amazon.com/images/I/71YvYl-f-aL._SL1500_.jpg"
    }
]

# 4. App Header
st.markdown('<div class="header-box">⚡ Delivery in 10 minutes to Phase 3</div>', unsafe_allow_html=True)
st.text_input("Search for groceries...", placeholder="Search 'Biscuits'", label_visibility="collapsed")

# 5. Product Grid (Bulletproof Layout)
st.subheader("Trending Today")
cols = st.columns(2)

for idx, item in enumerate(catalog):
    # Notice the strict indentation here under 'with cols'
    with cols[idx % 2]:
        st.markdown(f'<span class="discount-badge">{item["off"]}</span>', unsafe_allow_html=True)
        st.image(item["url"], use_container_width=True)
        st.write(f"**{item['name']}**")
        st.write(f"₹{item['price']}  ~~₹{item['mrp']}~~")
        st.button("ADD", key=f"add_{idx}", use_container_width=True)

# 6. Footer CTA
st.divider()
if st.button("🛒 View Cart & Checkout", use_container_width=True, type="primary"):
    st.balloons()
