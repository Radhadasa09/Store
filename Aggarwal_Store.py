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
#      MOBILE-FIRST CUSTOM CSS
# ==========================================
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #f4f6f8; }
    
    /* Category Card Styles */
    .cat-card {
        background: white;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .cat-img {
        width: 100%;
        height: 120px;
        object-fit: cover;
        border-radius: 8px;
    }
    
    /* Product Card Styles */
    .product-card {
        background: white;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 15px;
    }
    .product-image {
        height: 120px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 10px;
        width: 100%;
    }
    .price-text {
        font-weight: 800;
        color: #8b0000; 
        font-size: 1.3em;
        margin: 5px 0;
    }
    .product-name {
        font-weight: 600;
        color: #333;
        font-size: 0.95em;
        height: 45px;
        overflow: hidden;
    }
    
    /* Blinkit Green Buttons */
    .stButton>button {
        background-color: #0c831f; 
        color: white !important;
        border-radius: 8px;
        font-weight: 700;
        border: none;
        width: 100%;
    }
    .stButton>button:hover { background-color: #0a6b19; }
    
    /* Secondary/Navigation Buttons */
    div[data-testid="stHorizontalBlock"] button {
        background-color: white;
        color: #8b0000 !important;
        border: 1px solid #8b0000;
    }
    div[data-testid="stHorizontalBlock"] button:hover {
        background-color: #8b0000;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State ---
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'active_section' not in st.session_state:
    st.session_state.active_section = "Home"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def change_section(section_name):
    st.session_state.active_section = section_name

def add_to_cart(item):
    st.session_state.cart.append(item)
    st.toast(f"Added {item['name']} to cart! 🛒")

# ==========================================
#   STABLE IMAGE DATA (Unsplash)
# ==========================================
categories = {
    # UPDATED: Supermarket aisle with packaged goods, no vegetables!
    "Grocery": "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=400",
    "Baby Care": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=400",
    "Stationery": "https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=400",
    "Ice Creams": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=400"
}

products = [
    {"id": 1, "name": "Fresh Milk (500ml)", "price": 27, "category": "Grocery", "img_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=400"},
    {"id": 2, "name": "Brown Bread", "price": 40, "category": "Grocery", "img_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400"},
    {"id": 3, "name": "Notebook (172 Pgs)", "price": 50, "category": "Stationery", "img_url": "https://images.unsplash.com/photo-1531346878377-a5be20888e57?w=400"},
    {"id": 4, "name": "Baby Diapers (30 Pcs)", "price": 399, "category": "Baby Care", "img_url": "https://images.unsplash.com/photo-1522771930-78848d9293e8?w=400"},
    {"id": 5, "name": "Chocolate Cone", "price": 50, "category": "Ice Creams", "img_url": "https://images.unsplash.com/photo-1558500851-460d3f8fba3a?w=400"},
]

# --- Sidebar (Hidden by default, used for Owner Access) ---
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
        
        # 2x2 Grid for Mobile Friendliness
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
        # Back Button & Title
        st.button("← Back to Home", on_click=change_section, args=("Home",))
        st.subheader(f"🛒 {st.session_state.active_section}")
        
        # Filter products by active section
        section_products = [p for p in products if p['category'] == st.session_state.active_section]
        
        if not section_products:
            st.info(f"No products currently available in {st.session_state.active_section}.")
            
        # Display Products in 2 Columns (Perfect for Mobile screens)
        pc1, pc2 = st.columns(2)
        for i, product in enumerate(section_products):
            col = pc1 if i % 2 == 0 else pc2
            with col:
                st.markdown(f"""
                    <div class="product-card">
                        <img src='{product['img_url']}' class='product-image' />
                        <p class='product-name'>{product['name']}</p>
                        <p class="price-text">₹{product['price']}</p>
                    </div>
                """, unsafe_allow_html=True)
                st.button("ADD", key=f"add_{product['id']}", on_click=add_to_cart, args=(product,), use_container_width=True)
        
        st.divider()
        # BOTTOM NAVIGATION - Jump to other sections
        st.markdown("**Shop other categories:**")
        nav_cols = st.columns(3)
        nav_idx = 0
        for cat in categories.keys():
            if cat != st.session_state.active_section:
                with nav_cols[nav_idx % 3]:
                    st.button(cat, key=f"nav_{cat}", on_click=change_section, args=(cat,), use_container_width=True)
                nav_idx += 1

    st.divider()
    
    # --- MOBILE BOTTOM STACK: CART & CHATBOT ---
    st.markdown("<div id='your-cart'></div>", unsafe_allow_html=True) # Anchor for jump link
    
    st.markdown("### 🛒 Your Cart")
    with st.container(border=True):
        if not st.session_state.cart:
            st.info("Your cart is empty.")
        else:
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_summary = cart_df.groupby(['name', 'price']).size().reset_index(name='qty')
            cart_summary['total'] = cart_summary['price'] * cart_summary['qty']
            
            for _, row in cart_summary.iterrows():
                st.write(f"**{row['qty']}x** {row['name']} : **₹{row['total']}**")
            
            subtotal = cart_summary['total'].sum()
            delivery_fee = 0 if subtotal >= 250 else 30
            st.divider()
            st.write(f"**Subtotal:** ₹{subtotal}")
            if delivery_fee == 0:
                st.success("🚚 FREE Delivery Applied!")
            else:
                st.warning(f"Delivery: ₹30 (Add ₹{250-subtotal} more for free delivery)")
            
            st.markdown(f"<h3 style='color:#8b0000;'>Total: ₹{subtotal + delivery_fee}</h3>", unsafe_allow_html=True)
            st.button("Checkout & Pay", type="primary", use_container_width=True)

    # Chatbot Area
    st.markdown("### 💬 Dukaan Assistant")
    with st.expander("Have a question? Open Chatbot"):
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"👤 **You:** {msg['text']}")
            else:
                st.success(f"🏪 **Bot:** {msg['text']}")
        
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_input("Ask about products, delivery, or Khata...")
            if st.form_submit_button("Send") and user_input:
                st.session_state.chat_history.append({"role": "user", "text": user_input})
                if "khata" in user_input.lower():
                    response = "You can choose 'Pay Later' at checkout to add this to your monthly Khata balance!"
                else:
                    response = "I will pass this to the store owner! Delivery is free above ₹250."
                st.session_state.chat_history.append({"role": "bot", "text": response})
                st.rerun()

# ==========================================
#          OWNER DASHBOARD VIEW (Hidden in Sidebar)
# ==========================================
elif app_mode == "💻 Dashboard":
    st.title("🏪 Owner Dashboard")
    st.info("The dashboard is active. Switch back to 'Storefront' in the sidebar to view the customer app.")
    
    # --- Owner Dashboard Logic ---
    st.markdown("### Today's Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="Today's Sales", value="₹4,250", delta="+₹450")
    with col2: st.metric(label="Pending Deliveries", value="4", delta="-1")
    with col3: st.metric(label="Outstanding Khata", value="₹12,500", delta="-₹200", delta_color="inverse")
    
    if 'wallet_balance' not in st.session_state:
        st.session_state.wallet_balance = 425.50
        
    with col4: st.metric(label="Platform Wallet", value=f"₹{st.session_state.wallet_balance:.2f}")

    if st.session_state.wallet_balance < 500:
        st.error(f"⚠️ **Low Wallet Balance**: Please recharge your platform wallet to keep accepting Home Delivery orders.")

    tab1, tab2, tab3 = st.tabs(["📦 Active Orders", "📖 Khata Ledger", "💳 Wallet & Billing"])

    with tab1:
        st.subheader("Live Delivery Orders")
        orders = pd.DataFrame({
            "Order ID": ["#1042", "#1043", "#1044"],
            "Customer": ["Rahul M.", "Priya S.", "Amit K."],
            "Amount": ["₹280", "₹150", "₹320"],
            "Status": ["Packing", "Ready", "Out for Delivery"]
        })
        st.dataframe(orders, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Digital Khata (Credit Customers)")
        khata_data = pd.DataFrame({
            "Customer": ["Vikram Singh", "Neha Gupta"],
            "Outstanding": ["₹4,500", "₹1,200"],
            "Last Paid": ["12 Days Ago", "5 Days Ago"]
        })
        st.dataframe(khata_data, use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("Platform Wallet History")
        st.info("**Pricing Tier Active:** 3% fee on Home Deliveries | 1% fee on Khata settlements.")
        if st.button("Simulate ₹1000 Recharge", type="primary"):
            st.session_state.wallet_balance += 1000
            st.rerun()
