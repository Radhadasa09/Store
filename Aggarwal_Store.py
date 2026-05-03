import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Aggarwal Store | Premium",
    page_icon="🛍️",
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# ==========================================
#   PREMIUM UX/UI CSS (Startup Grade)
# ==========================================
st.markdown("""
    <style>
    /* Import Premium Startup Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * { font-family: 'Inter', sans-serif !important; }
    
    /* Clean, ultra-light grey background */
    [data-testid="stAppViewContainer"] { background-color: #F9FAFB; }
    
    /* Premium Gradient Top Banner */
    .top-banner {
        background: linear-gradient(135deg, #7f1d1d 0%, #b91c1c 100%);
        color: white;
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(185, 28, 28, 0.2);
    }
    .top-banner h1 { color: white; font-weight: 800; margin: 0; font-size: 2.4em; letter-spacing: -1px; }
    .top-banner p { margin: 6px 0 0 0; font-size: 1.1em; opacity: 0.9; font-weight: 500; }
    
    /* Apple-Style Soft Cards */
    .cat-card, .product-card, div[data-testid="stVerticalBlock"] > div > div {
        background: #ffffff !important;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.04) !important;
        border: none !important;
    }
    
    /* Category Grid Styling */
    .cat-card { padding: 8px; text-align: center; margin-bottom: 12px; transition: transform 0.2s ease; cursor: pointer; }
    .cat-card:active { transform: scale(0.96); }
    .cat-img { width: 100%; height: 130px; object-fit: cover; border-radius: 12px; }
    .cat-title { margin: 12px 0 6px 0; color: #111827; font-weight: 700; font-size: 1.05em; }
    
    /* Product Card Styling */
    .product-card { padding: 18px; text-align: center; margin-bottom: 20px; position: relative; }
    .product-image { height: 130px; object-fit: contain; margin-bottom: 15px; width: 100%; transition: transform 0.3s ease; }
    .product-card:hover .product-image { transform: scale(1.05); }
    
    /* Pricing & Badges */
    .price-text { font-weight: 800; color: #111827; font-size: 1.4em; margin: 5px 0 0 0; }
    .mrp-text { font-weight: 500; color: #9CA3AF; font-size: 0.75em; text-decoration: line-through; margin-left: 6px; }
    .discount-badge {
        position: absolute; top: 12px; left: 12px;
        background-color: #3B82F6; color: white;
        font-size: 0.7em; font-weight: 700; padding: 4px 10px; border-radius: 20px;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3);
    }
    
    .product-name { font-weight: 600; color: #374151; font-size: 0.95em; height: 42px; overflow: hidden; line-height: 1.4; }
    
    /* Premium Action Buttons */
    .stButton>button { 
        background-color: #10B981; /* Premium Zepto/Blinkit Green */
        color: white !important; 
        border-radius: 12px; 
        font-weight: 700; 
        border: none; 
        width: 100%; 
        padding: 12px 0; 
        transition: all 0.2s;
    }
    .stButton>button:hover { background-color: #059669; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3); }
    .stButton>button:active { transform: scale(0.97); }
    
    /* Jump to Cart Floating Pill */
    .jump-pill {
        display: block; text-align: center; margin: -10px auto 25px auto;
        font-weight: 700; color: #7f1d1d; text-decoration: none;
        background: #FEF2F2; padding: 12px 24px; border-radius: 30px;
        width: fit-content; border: 1px solid #FCA5A5;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State ---
if 'cart' not in st.session_state: st.session_state.cart = []
if 'active_section' not in st.session_state: st.session_state.active_section = "Home"

def change_section(section_name): st.session_state.active_section = section_name

def add_to_cart(item):
    st.session_state.cart.append(item)
    st.toast(f"Added {item['name']} to cart! 🛒")

# ==========================================
#   PREMIUM INVENTORY (High-Res Amazon URLs)
# ==========================================
categories = {
    "Dairy & Milk": "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=400&q=80", # Clean milk splash
    "Snacks & Namkeen": "https://images.unsplash.com/photo-1600137583648-522167d45749?w=400&q=80", # Premium snack bowl
    "Cold Drinks": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400&q=80", # Sleek fridge drinks
    "Pulses & Dal": "https://images.unsplash.com/photo-1585942423984-63f25ceb22bd?w=400&q=80", # Premium lentils
    "Baby Care": "https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400&q=80" # Clean baby aesthetic
}

products = [
    # Dairy
    {"id": 1, "name": "Amul Taaza Toned Milk (500ml)", "mrp": 27, "price": 27, "category": "Dairy & Milk", "img_url": "https://m.media-amazon.com/images/I/61k1qHwA2bL._SX679_.jpg"},
    {"id": 2, "name": "Amul Gold Full Cream (500ml)", "mrp": 33, "price": 33, "category": "Dairy & Milk", "img_url": "https://m.media-amazon.com/images/I/61-d7+A85hL._SX679_.jpg"},
    # Snacks
    {"id": 5, "name": "Haldiram's Bhujia Sev (400g)", "mrp": 110, "price": 99, "category": "Snacks & Namkeen", "img_url": "https://m.media-amazon.com/images/I/71YV6H+d+4L._SX679_.jpg"},
    {"id": 6, "name": "Lay's India's Magic Masala", "mrp": 20, "price": 18, "category": "Snacks & Namkeen", "img_url": "https://m.media-amazon.com/images/I/61XzQ-h2XoL._SX679_.jpg"},
    {"id": 7, "name": "Kurkure Masala Munch (90g)", "mrp": 20, "price": 18, "category": "Snacks & Namkeen", "img_url": "https://m.media-amazon.com/images/I/71L5IytM1PL._SX679_.jpg"},
    # Drinks
    {"id": 8, "name": "Thums Up Soft Drink (750ml)", "mrp": 45, "price": 40, "category": "Cold Drinks", "img_url": "https://m.media-amazon.com/images/I/615a9v+ZkcL._SX679_.jpg"},
    {"id": 9, "name": "Sprite Clear Lime (750ml)", "mrp": 45, "price": 40, "category": "Cold Drinks", "img_url": "https://m.media-amazon.com/images/I/51bVwzL3jUL._SX679_.jpg"},
    # Pulses
    {"id": 11, "name": "Tata Sampann Toor Dal (1kg)", "mrp": 215, "price": 185, "category": "Pulses & Dal", "img_url": "https://m.media-amazon.com/images/I/61tM0U0s3vL._SX679_.jpg"},
    # Baby
    {"id": 13, "name": "Huggies Wonder Pants (M, 30s)", "mrp": 499, "price": 399, "category": "Baby Care", "img_url": "https://m.media-amazon.com/images/I/61x0YQjJvYL._SX679_.jpg"}
]

# --- Sidebar ---
st.sidebar.markdown("### 🏬 Store Management")
app_mode = st.sidebar.radio("Interface", ["📱 Storefront", "💻 Dashboard"])

# ==========================================
#        CUSTOMER STOREFRONT VIEW
# ==========================================
if app_mode == "📱 Storefront":
    
    # Premium Top Banner
    st.markdown("""
        <div class="top-banner">
            <h1>Aggarwal Store</h1>
            <p>⚡ Superfast Delivery in Phase 3</p>
        </div>
    """, unsafe_allow_html=True)

    # Pill-shaped jump link
    st.markdown("<a href='#your-cart' class='jump-pill'>🛒 View Cart & Checkout</a>", unsafe_allow_html=True)

    # --- VIEW 1: HOME (CATEGORY GRID) ---
    if st.session_state.active_section == "Home":
        st.markdown("<h3 style='color:#111827; margin-bottom:15px; font-weight:700;'>Shop by Category</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        cat_names = list(categories.keys())
        
        for i, cat in enumerate(cat_names):
            col = c1 if i % 2 == 0 else c2
            with col:
                st.markdown(f"""
                    <div class="cat-card">
                        <img src="{categories[cat]}" class="cat-img"/>
                        <div class="cat-title">{cat}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.button(f"Explore", key=f"btn_{cat}", on_click=change_section, args=(cat,), use_container_width=True)

    # --- VIEW 2: INSIDE A SPECIFIC SECTION ---
    else:
        st.button("← Back to Categories", on_click=change_section, args=("Home",))
        st.markdown(f"<h3 style='color:#111827; margin: 15px 0; font-weight:800;'>{st.session_state.active_section}</h3>", unsafe_allow_html=True)
        
        section_products = [p for p in products if p['category'] == st.session_state.active_section]
        
        pc1, pc2 = st.columns(2)
        for i, product in enumerate(section_products):
            col = pc1 if i % 2 == 0 else pc2
            with col:
                discount = 0
                badge_html = ""
                if product['mrp'] > product['price']:
                    discount = round(((product['mrp'] - product['price']) / product['mrp']) * 100)
                    badge_html = f"<span class='discount-badge'>{discount}% OFF</span>"
                
                st.markdown(f"""
                    <div class="product-card">
                        {badge_html}
                        <img src='{product['img_url']}' class='product-image' />
                        <p class='product-name'>{product['name']}</p>
                        <p class="price-text">₹{product['price']} <span class="mrp-text">₹{product['mrp']}</span></p>
                    </div>
                """, unsafe_allow_html=True)
                st.button("ADD", key=f"add_{product['id']}", on_click=add_to_cart, args=(product,), use_container_width=True)

    st.divider()
    
    # --- MOBILE BOTTOM STACK: CART WITH SAVINGS ---
    st.markdown("<div id='your-cart'></div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color:#111827; font-weight:800;'>🛒 Order Summary</h3>", unsafe_allow_html=True)
    with st.container():
        if not st.session_state.cart:
            st.info("Your cart is empty. Start shopping!")
        else:
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_summary = cart_df.groupby(['name', 'price', 'mrp']).size().reset_index(name='qty')
            cart_summary['total_price'] = cart_summary['price'] * cart_summary['qty']
            cart_summary['total_mrp'] = cart_summary['mrp'] * cart_summary['qty']
            
            for _, row in cart_summary.iterrows():
                st.markdown(f"<div style='font-size:1.05em; margin-bottom:8px;'><b>{row['qty']}x</b> {row['name'][:22]}... <span style='float:right; font-weight:800;'>₹{row['total_price']}</span></div>", unsafe_allow_html=True)
            
            subtotal_price = cart_summary['total_price'].sum()
            subtotal_mrp = cart_summary['total_mrp'].sum()
            total_savings = subtotal_mrp - subtotal_price
            delivery_fee = 0 if subtotal_price >= 250 else 30
            
            st.divider()
            st.markdown(f"<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><span style='color:#6B7280;'>Total MRP</span><span>₹{subtotal_mrp}</span></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><span style='color:#6B7280;'>Store Discount</span><span style='color:#10B981; font-weight:700;'>-₹{total_savings}</span></div>", unsafe_allow_html=True)
            
            if delivery_fee == 0:
                st.markdown(f"<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><span style='color:#6B7280;'>Delivery Fee</span><span style='color:#10B981; font-weight:700;'>FREE</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><span style='color:#6B7280;'>Delivery Fee</span><span>₹{delivery_fee}</span></div>", unsafe_allow_html=True)
                st.caption(f"Add ₹{250-subtotal_price} more for free delivery")
            
            st.divider()
            st.markdown(f"<h2 style='color:#111827; text-align:center; margin:0;'>To Pay: ₹{subtotal_price + delivery_fee}</h2>", unsafe_allow_html=True)
            if total_savings > 0:
                st.markdown(f"<div style='text-align:center; color:#10B981; font-weight:700; margin: 10px 0 20px 0; background:#D1FAE5; padding:8px; border-radius:8px;'>🎉 You save ₹{total_savings} on this order!</div>", unsafe_allow_html=True)
            
            st.button("Proceed to Pay", type="primary", use_container_width=True)

# ==========================================
#          OWNER DASHBOARD VIEW (Unchanged)
# ==========================================
elif app_mode == "💻 Dashboard":
    st.title("Owner Dashboard")
    st.info("Dashboard active. Switch to 'Storefront' to see the newly updated Premium UI.")
