import streamlit as st

# 1. SETUP & BRANDING
st.set_page_config(page_title="Aggarwal Store | Fast Delivery", layout="centered", page_icon="⚡")

# Initialize Session State for the Cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# 2. MARKETING-DRIVEN CSS
st.markdown("""
<style>
    /* Blinkit Brand Colors */
    :root {
        --blinkit-yellow: #F7D106;
        --blinkit-green: #0C831F;
    }
    .main { background-color: #f8f9fa; }
    
    /* Header & Banners */
    .delivery-header {
        background-color: var(--blinkit-yellow);
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: 800;
        font-size: 1.1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Product Card Styling */
    div[data-testid="stColumn"] {
        background: white;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #eee;
        transition: transform 0.2s;
    }
    div[data-testid="stColumn"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* Add Button Styling */
    .stButton>button {
        background-color: var(--blinkit-green) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
        font-weight: 700;
        height: 45px;
    }
    
    /* Discount Badge */
    .badge {
        background: #2563eb;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# 3. PRODUCT CATALOG
# Using stable, high-res links for the best visual appetite
products = [
    {"id": 1, "name": "Haldiram's Bhujia Sev", "spec": "400g", "price": 99, "mrp": 110, "off": "10% OFF", "img": "https://m.media-amazon.com/images/I/81vJ9S-Z7VL._SL1500_.jpg", "cat": "Snacks"},
    {"id": 2, "name": "Thums Up (Chilled)", "spec": "750ml", "price": 40, "mrp": 45, "off": "11% OFF", "img": "https://m.media-amazon.com/images/I/610C86pY6DL._SL1500_.jpg", "cat": "Drinks"},
    {"id": 3, "name": "Good Day Cashew", "spec": "600g", "price": 120, "mrp": 140, "off": "14% OFF", "img": "https://m.media-amazon.com/images/I/71YvYl-f-aL._SL1500_.jpg", "cat": "Snacks"},
    {"id": 4, "name": "Amul Taaza Milk", "spec": "1L", "price": 54, "mrp": 56, "off": "3% OFF", "img": "https://m.media-amazon.com/images/I/51-u0B-O3vL._SL1000_.jpg", "cat": "Dairy"}
]

# 4. APP LAYOUT
# Top Header - Leveraging Gurgaon context for trust
st.markdown('<div class="delivery-header">⚡ Delivery to Gurgaon Phase 3 in 9 mins</div>', unsafe_allow_html=True)

# Search Bar
search_query = st.text_input("", placeholder="Search for 'milk' or 'chips'...", label_visibility="collapsed")

# Category Quick-Links
st.write("### Shop by Category")
cat_cols = st.columns(4)
categories = ["Snacks", "Drinks", "Dairy", "Luxury"] # Added 'Luxury' for future rental brand alignment
for i, cat in enumerate(categories):
    cat_cols[i].button(cat, use_container_width=True, key=f"cat_{cat}")

st.divider()

# 5. PRODUCT GRID
st.subheader("Trending in your area")
grid_cols = st.columns(2)

for idx, p in enumerate(products):
    # Search Filter
    if search_query.lower() in p["name"].lower():
        with grid_cols[idx % 2]:
            st.markdown(f'<span class="badge">{p["off"]}</span>', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.write(f"**{p['name']}**")
            st.caption(p["spec"])
            st.markdown(f"**₹{p['price']}** <span style='color:gray; text-decoration:line-through; font-size:12px;'>₹{p['mrp']}</span>", unsafe_allow_html=True)
            
            if st.button("ADD", key=f"btn_{p['id']}"):
                # Add to cart logic
                item_name = p["name"]
                st.session_state.cart[item_name] = st.session_state.cart.get(item_name, 0) + 1
                st.toast(f"Added {item_name} to cart!", icon="🛒")

# 6. DYNAMIC SIDEBAR CART (The "Impressive" Touch)
with st.sidebar:
    st.title("My Basket 🛒")
    if not st.session_state.cart:
        st.write("Your basket is empty. Start adding!")
    else:
        total = 0
        for item, qty in st.session_state.cart.items():
            # Find price for total
            price = next(p["price"] for p in products if p["name"] == item)
            total += price * qty
            st.write(f"**{item}** x {qty} = ₹{price * qty}")
        
        st.divider()
        st.write(f"### Total: ₹{total}")
        if st.button("Checkout Now", type="primary", use_container_width=True):
            st.balloons()
            st.success("Order placed successfully for Phase 3!")
            st.session_state.cart = {} # Reset cart

    st.divider()
    st.info("Aggarwal Store: Proudly serving Gurgaon residents with 100% compliance.")
