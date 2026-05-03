import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Aggarwal Store",
    page_icon="🏪",
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# ==========================================
#   SHOPPING MALL THEME & CUSTOM CSS
# ==========================================
st.markdown("""
    <style>
    /* Shopping Mall Blurred Background */
    [data-testid="stAppViewContainer"] { 
        background-image: url("https://images.unsplash.com/photo-1542838132-92c53300491e?w=1600&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* Overlay to make background less distracting */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(244, 246, 248, 0.85); /* Light frost effect */
        z-index: -1;
    }
    
    /* Transparent Floating Cards */
    .cat-card, .product-card, .stContainer > div {
        background: rgba(255, 255, 255, 0.95) !important; /* Mostly white, slight transparency */
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    
    .cat-card { padding: 10px; text-align: center; margin-bottom: 10px; }
    .cat-img { width: 100%; height: 120px; object-fit: cover; border-radius: 8px; }
    
    .product-card {
        padding: 15px; text-align: center; margin-bottom: 15px; position: relative;
    }
    .product-image { height: 110px; object-fit: contain; margin-bottom: 10px; width: 100%; }
    
    /* Pricing & MRP Styles */
    .price-text { font-weight: 800; color: #8b0000; font-size: 1.3em; margin: 5px 0 0 0; }
    .mrp-text { font-weight: 500; color: #888; font-size: 0.7em; text-decoration: line-through; margin-left: 5px; }
    .discount-badge {
        position: absolute; top: 10px; left: 10px;
        background-color: #28a745; color: white;
        font-size: 0.7em; font-weight: bold; padding: 3px 8px; border-radius: 4px;
    }
    
    .product-name { font-weight: 600; color: #333; font-size: 0.95em; height: 40px; overflow: hidden; }
    
    /* Buttons */
    .stButton>button { background-color: #0c831f; color: white !important; border-radius: 8px; font-weight: 700; border: none; width: 100%; }
    .stButton>button:hover { background-color: #0a6b19; }
    div[data-testid="stHorizontalBlock"] button { background-color: white; color: #8b0000 !important; border: 1px solid #8b0000; }
    div[data-testid="stHorizontalBlock"] button:hover { background-color: #8b0000; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- Session State ---
if 'cart' not in st.session_state: st.session_state.cart = []
if 'active_section' not in st.session_state: st.session_state.active_section = "Home"
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

def change_section(section_name): st.session_state.active_section = section_name

def add_to_cart(item):
    st.session_state.cart.append(item)
    st.toast(f"Added {item['name']} to cart! 🛒")

# ==========================================
#   EXPANDED INVENTORY (Gurgaon Store Mix)
# ==========================================
categories = {
    "Dairy & Milk": "https://images.unsplash.com/photo-1628088062854-d1870b4553da?w=400",
    "Snacks & Namkeen": "https://images.unsplash.com/photo-1599490659213-e2b9527bd087?w=400",
    "Cold Drinks": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    "Pulses & Dal": "https://images.unsplash.com/photo-1585942423984-63f25ceb22bd?w=400",
    "Baby Care": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=400"
}

# Products now include 'mrp' and 'price' (Selling Price)
products = [
    # Dairy & Milk (Amul Variations)
    {"id": 1, "name": "Amul Taaza Toned Milk (500ml)", "mrp": 27, "price": 27, "category": "Dairy & Milk", "img_url": "https://www.bigbasket.com/media/uploads/p/l/104618_7-amul-taaza-toned-milk.jpg"},
    {"id": 2, "name": "Amul Gold Full Cream (500ml)", "mrp": 33, "price": 33, "category": "Dairy & Milk", "img_url": "https://www.bigbasket.com/media/uploads/p/l/1222474_1-amul-gold-homogenised-standardised-milk.jpg"},
    {"id": 3, "name": "Amul Cow Milk (500ml)", "mrp": 28, "price": 28, "category": "Dairy & Milk", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40005030_2-amul-cow-milk.jpg"},
    {"id": 4, "name": "Amul Buffalo Milk (500ml)", "mrp": 35, "price": 35, "category": "Dairy & Milk", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40202165_3-amul-buffalo-milk.jpg"},
    
    # Snacks & Namkeen (Local Favorites)
    {"id": 5, "name": "Haldiram's Bhujia Sev (400g)", "mrp": 110, "price": 99, "category": "Snacks & Namkeen", "img_url": "https://www.bigbasket.com/media/uploads/p/l/264491_5-haldirams-namkeen-bhujia-sev.jpg"},
    {"id": 6, "name": "Lay's India's Magic Masala", "mrp": 20, "price": 18, "category": "Snacks & Namkeen", "img_url": "https://www.bigbasket.com/media/uploads/p/l/293667_13-lays-potato-chips-indias-magic-masala.jpg"},
    {"id": 7, "name": "Kurkure Masala Munch (90g)", "mrp": 20, "price": 18, "category": "Snacks & Namkeen", "img_url": "https://www.bigbasket.com/media/uploads/p/l/294297_15-kurkure-namkeen-masala-munch.jpg"},
    
    # Cold Drinks
    {"id": 8, "name": "Thums Up Soft Drink (750ml)", "mrp": 45, "price": 40, "category": "Cold Drinks", "img_url": "https://www.bigbasket.com/media/uploads/p/l/251023_8-thums-up-soft-drink.jpg"},
    {"id": 9, "name": "Frooti Mango Drink (1.2L)", "mrp": 70, "price": 60, "category": "Cold Drinks", "img_url": "https://www.bigbasket.com/media/uploads/p/l/265819_8-frooti-mango-drink.jpg"},
    {"id": 10, "name": "Sprite Clear (750ml)", "mrp": 45, "price": 40, "category": "Cold Drinks", "img_url": "https://www.bigbasket.com/media/uploads/p/l/251014_11-sprite-soft-drink-lime-flavoured.jpg"},
    
    # Pulses
    {"id": 11, "name": "Tata Sampann Toor Dal (1kg)", "mrp": 215, "price": 185, "category": "Pulses & Dal", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40000291_9-tata-sampann-unpolished-toor-dal-arhar-dal.jpg"},
    {"id": 12, "name": "Rajdhani Moong Dal (500g)", "mrp": 85, "price": 75, "category": "Pulses & Dal", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40058866_3-rajdhani-moong-dal-yellow.jpg"},
    
    # Baby Care
    {"id": 13, "name": "Huggies Wonder Pants (M, 30s)", "mrp": 499, "price": 399, "category": "Baby Care", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40131014_8-huggies-wonder-pants-diapers-medium-m.jpg"}
]

# --- Sidebar (Hidden by default) ---
st.sidebar.markdown("### 🏬 Store Management")
app_mode = st.sidebar.radio("Interface", ["📱 Storefront", "💻 Dashboard"])

# ==========================================
#        CUSTOMER STOREFRONT VIEW
# ==========================================
if app_mode == "📱 Storefront":
    
    # Header Area
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h2 style='color: #8b0000; margin-bottom: 0;'>🏪 Aggarwal Store</h2>", unsafe_allow_html=True)
        st.caption("📍 Phase 3 • Delivery in 10 mins")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("[Jump to Cart 🛒](#your-cart)")

    st.divider()

    # --- VIEW 1: HOME (CATEGORY GRID) ---
    if st.session_state.active_section == "Home":
        st.subheader("What are you looking for?")
        c1, c2 = st.columns(2)
        cat_names = list(categories.keys())
        
        for i, cat in enumerate(cat_names):
            col = c1 if i % 2 == 0 else c2
            with col:
                st.markdown(f"""
                    <div class="cat-card">
                        <img src="{categories[cat]}" class="cat-img"/>
                        <h4 style="margin: 10px 0 5px 0; color: #333;">{cat}</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.button(f"Shop {cat}", key=f"btn_{cat}", on_click=change_section, args=(cat,), use_container_width=True)

    # --- VIEW 2: INSIDE A SPECIFIC SECTION ---
    else:
        st.button("← Back to Home", on_click=change_section, args=("Home",))
        st.subheader(f"🛒 {st.session_state.active_section}")
        
        section_products = [p for p in products if p['category'] == st.session_state.active_section]
        
        pc1, pc2 = st.columns(2)
        for i, product in enumerate(section_products):
            col = pc1 if i % 2 == 0 else pc2
            with col:
                # Calculate discount percentage
                discount = 0
                badge_html = ""
                if product['mrp'] > product['price']:
                    discount = round(((product['mrp'] - product['price']) / product['mrp']) * 100)
                    badge_html = f"<span class='discount-badge'>{discount}% OFF</span>"
                
                # Render HTML with MRP and Price
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
        st.markdown("**Shop other categories:**")
        nav_cols = st.columns(3)
        nav_idx = 0
        for cat in categories.keys():
            if cat != st.session_state.active_section:
                with nav_cols[nav_idx % 3]:
                    st.button(cat[:10]+"..", key=f"nav_{cat}", on_click=change_section, args=(cat,), use_container_width=True)
                nav_idx += 1

    st.divider()
    
    # --- MOBILE BOTTOM STACK: CART WITH SAVINGS ---
    st.markdown("<div id='your-cart'></div>", unsafe_allow_html=True)
    
    st.markdown("### 🛒 Your Cart")
    with st.container():
        if not st.session_state.cart:
            st.info("Your cart is empty.")
        else:
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_summary = cart_df.groupby(['name', 'price', 'mrp']).size().reset_index(name='qty')
            cart_summary['total_price'] = cart_summary['price'] * cart_summary['qty']
            cart_summary['total_mrp'] = cart_summary['mrp'] * cart_summary['qty']
            
            # Print items
            for _, row in cart_summary.iterrows():
                st.write(f"**{row['qty']}x** {row['name'][:20]}... : **₹{row['total_price']}**")
            
            # Calculate Totals
            subtotal_price = cart_summary['total_price'].sum()
            subtotal_mrp = cart_summary['total_mrp'].sum()
            total_savings = subtotal_mrp - subtotal_price
            delivery_fee = 0 if subtotal_price >= 250 else 30
            
            st.divider()
            # The Bill Breakdown
            c_bill1, c_bill2 = st.columns([3, 1])
            c_bill1.write("Total MRP:")
            c_bill2.write(f"₹{subtotal_mrp}")
            
            c_bill1.write("Store Discount:")
            c_bill2.markdown(f"<span style='color:green;'>-₹{total_savings}</span>", unsafe_allow_html=True)
            
            if delivery_fee == 0:
                c_bill1.write("Delivery Fee:")
                c_bill2.markdown("<span style='color:green;'>FREE</span>", unsafe_allow_html=True)
                st.success("🚚 FREE Delivery Applied!")
            else:
                c_bill1.write("Delivery Fee:")
                c_bill2.write(f"₹{delivery_fee}")
                st.warning(f"Add ₹{250-subtotal_price} more for free delivery")
            
            st.divider()
            st.markdown(f"<h3 style='color:#8b0000; margin:0;'>To Pay: ₹{subtotal_price + delivery_fee}</h3>", unsafe_allow_html=True)
            if total_savings > 0:
                st.markdown(f"<p style='color:#0c831f; font-weight:bold; margin-top:0;'>🎉 You save ₹{total_savings} on this order!</p>", unsafe_allow_html=True)
            
            st.button("Checkout & Pay", type="primary", use_container_width=True)

# ==========================================
#          OWNER DASHBOARD VIEW (Unchanged)
# ==========================================
elif app_mode == "💻 Dashboard":
    st.title("🏪 Owner Dashboard")
    # ... [Dashboard logic stays the same] ...
    st.info("Dashboard active. Switch to 'Storefront' to see the new inventory and mall theme.")
