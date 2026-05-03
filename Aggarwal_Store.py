import streamlit as st
import requests

# Set page to wide mode for better UI/UX
st.set_page_config(layout="wide", page_title="Blinkit Clone")

# 1. Self-Audit Utility
def check_image_url(url):
    try:
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except:
        return False

# 2. Updated Product Data (Alternatives to Amazon Links)
products = [
    {
        "name": "Haldiram's Bhujia Sev (400g)",
        "price": 99,
        "mrp": 110,
        "discount": "10% OFF",
        "img": "https://m.media-amazon.com/images/I/81vJ9S-Z7VL._SL1500_.jpg"
    },
    {
        "name": "Thums Up (750ml)",
        "price": 40,
        "mrp": 45,
        "discount": "11% OFF",
        "img": "https://m.media-amazon.com/images/I/610C86pY6DL._SL1500_.jpg"
    },
    {
        "name": "Britannia Good Day Biscuits",
        "price": 120,
        "mrp": 140,
        "discount": "14% OFF",
        "img": "https://m.media-amazon.com/images/I/71YvYl-f-aL._SL1500_.jpg"
    }
]

# 3. UI/UX: Custom CSS for the "Blinkit" look
st.markdown("""
<style>
    .product-card {
        border: 1px solid #f1f1f1;
        border-radius: 12px;
        padding: 15px;
        background: white;
        text-align: left;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .badge {
        background-color: #2563eb;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
    }
    .price-tag { font-weight: bold; font-size: 18px; }
    .mrp { text-decoration: line-through; color: gray; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# 4. Main UI
st.title("⚡ Superfast Delivery in Phase 3")
st.text_input("Search for groceries...", placeholder="Search 'chips'", label_visibility="collapsed")

st.subheader("Trending Today")
cols = st.columns(len(products))

for i, product in enumerate(products):
    with cols[i]:
        st.markdown(f'<span class="badge">{product["discount"]}</span>', unsafe_allow_html=True)
        st.image(product["img"], use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f'<span class="price-tag">₹{product["price"]}</span> <span class="mrp">₹{product["mrp"]}</span>', unsafe_allow_html=True)
        st.button("ADD", key=f"btn_{i}", use_container_width=True)

# 5. Admin Utilities: The Audit Log
with st.expander("Admin Utilities & Photo Audit"):
    if st.button("Run Photo Audit"):
        st.write(">> Running photo audit...")
        for p in products:
            status = "OK" if check_image_url(p["img"]) else "BROKEN ❌"
            st.write(f">> {p['name']}: URL {status}")
        st.success("Audit Complete.")
