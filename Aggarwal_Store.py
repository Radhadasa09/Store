import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Aggarwal Store - 10 Min Delivery",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
#      ENHANCED CUSTOM CSS (Blinkit Vibe)
# ==========================================
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #f4f6f8; } /* Cleaner, cooler background */
    
    .product-card {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        background-color: white;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative; /* For the bestseller badge */
    }
    .product-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.08);
        border-color: #8b0000;
    }
    .product-image {
        height: 110px;
        object-fit: contain;
        margin-bottom: 12px;
    }
    .price-text {
        font-weight: 700;
        color: #1a202c; 
        font-size: 1.2em;
        margin-top: 5px;
        margin-bottom: 10px;
    }
    .product-name {
        font-size: 0.95em;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 0px;
        height: 40px;
        overflow: hidden;
    }
    .badge {
        position: absolute;
        top: 10px;
        left: 10px;
        background-color: #ffc107;
        color: #000;
        font-size: 0.7em;
        font-weight: bold;
        padding: 3px 8px;
        border-radius: 4px;
    }
    .stButton>button {
        background-color: #0c831f; /* Quick-commerce Green */
        color: white !important;
        border-radius: 8px;
        font-weight: 700;
        border: none;
    }
    .stButton>button:hover { background-color: #0a6b19; }
    h1 { color: #8b0000; font-family: 'Inter', sans-serif; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 425.50
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# ==========================================
#   CORRECTED PRODUCT DATA
# ==========================================
products = [
    {"id": 1, "name": "Amul Taaza Toned Milk (500ml)", "price": 27, "category": "Grocery", "badge": "Fast Selling", "img_url": "https://www.bigbasket.com/media/uploads/p/l/104618_7-amul-taaza-toned-milk.jpg"},
    {"id": 2, "name": "Harvest Gold Brown Bread", "price": 40, "category": "Grocery", "badge": "", "img_url": "https://www.bigbasket.com/media/uploads/p/l/10000003_16-harvest-gold-brown-bread.jpg"},
    {"id": 3, "name": "Classmate Notebook (Unruled, 172 Pgs)", "price": 50, "category": "Stationery", "badge": "", "img_url": "https://www.bigbasket.com/media/uploads/p/l/293261_11-classmate-notebook-long-size-unruled-single-line.jpg"},
    {"id": 4, "name": "Huggies Wonder Pants (Medium, 30 Pcs)", "price": 399, "category": "Baby Care", "badge": "Offer", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40131014_8-huggies-wonder-pants-diapers-medium-m.jpg"}, # Moved Huggies here!
    {"id": 5, "name": "Kwality Wall's Cornetto Chocochip", "price": 50, "category": "Ice Creams", "badge": "", "img_url": "https://www.bigbasket.com/media/uploads/p/l/1212879_1-kwality-walls-cornetto-double-chocolush-frozen-dessert.jpg"},
    {"id": 6, "name": "Magnum Almond Ice Cream Stick", "price": 90, "category": "Ice Creams", "badge": "Bestseller", "img_url": "https://www.bigbasket.com/media/uploads/p/l/40003290_4-magnum-almond-ice-cream-stick.jpg"}
]

def add_to_cart(item):
    st.session_state.cart.append(item)

# --- Sidebar Navigation ---
st.sidebar.markdown("### 🏬 Aggarwal Store Nav")
app_mode = st.sidebar.radio("Choose Interface", ["📱 Customer Storefront", "💻 Owner Dashboard"])
st.sidebar.divider()

# ==========================================
#        CUSTOMER STOREFRONT VIEW
# ==========================================
if app_mode == "📱 Customer Storefront":
    st.title("🏪 Aggarwal Store")
    st.markdown("Delivery in **10 minutes** to your doorstep in Phase 3.")
    st.divider()

    search = st.text_input("Search for groceries, stationery, and more...", placeholder="Search 'Milk'")

    # Layout: Products (Left), Cart & Chatbot (Right)
    prod_col, right_col = st.columns([2.5, 1.2])

    with prod_col:
        st.subheader("Explore Categories")
        # Added Baby Care to the tabs
        tabs = st.tabs(["All Items", "Grocery", "Baby Care", "Stationery", "Ice Creams"])
        
        with tabs[0]:
            cols = st.columns(3)
            for index, product in enumerate(products):
                with cols[index % 3]:
                    badge_html = f"<span class='badge'>{product['badge']}</span>" if product['badge'] else ""
                    st.markdown(f"""
                        <div class="product-card">
                            {badge_html}
                            <img src='{product['img_url']}' class='product-image' />
                            <p class='product-name'>{product['name']}</p>
                            <p class="price-text">₹{product['price']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.button("ADD", key=f"add_{product['id']}", on_click=add_to_cart, args=(product,), use_container_width=True)

    # --- Right Column: Cart & Support Bot ---
    with right_col:
        # CART SECTION
        st.markdown("### 🛒 Your Cart")
        if not st.session_state.cart:
            st.info("Your cart is empty. Tap 'ADD' to start!")
        else:
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_summary = cart_df.groupby(['name', 'price']).size().reset_index(name='qty')
            cart_summary['total'] = cart_summary['price'] * cart_summary['qty']
            
            for _, row in cart_summary.iterrows():
                st.write(f"**{row['qty']}x** {row['name'][:15]}... - **₹{row['total']}**")
            
            subtotal = cart_summary['total'].sum()
            delivery_fee = 0 if subtotal >= 250 else 30
            st.divider()
            if delivery_fee == 0:
                st.success("🚚 FREE Delivery Unlocked!")
            else:
                st.warning(f"Add ₹{250-subtotal} more for free delivery")
            
            st.write(f"### **Total: ₹{subtotal + delivery_fee}**")
            st.button("Checkout (UPI / Khata)", type="primary", use_container_width=True)

        st.divider()

        # CHATBOT SECTION
        st.markdown("### 💬 Need Help?")
        with st.container(border=True):
            st.markdown("**Aggarwal Store Bot**")
            st.caption("Replies instantly")
            
            # Display chat history
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['text']}")
                else:
                    st.info(f"🤖 {msg['text']}")
            
            # Chat Input Form
            with st.form("chat_form", clear_on_submit=True):
                user_input = st.text_input("Ask a question...", placeholder="Do you have whole wheat bread?")
                submit_btn = st.form_submit_button("Send")
                
                if submit_btn and user_input:
                    # Save user message
                    st.session_state.chat_history.append({"role": "user", "text": user_input})
                    
                    # Simple Bot Logic
                    if "khata" in user_input.lower() or "credit" in user_input.lower():
                        response = "You can choose 'Pay Later' at checkout to add this to your monthly Khata balance!"
                    elif "delivery" in user_input.lower():
                        response = "We deliver within 10 minutes in the local area. Delivery is free for orders over ₹250!"
                    else:
                        response = "I will check with the store owner! In the meantime, feel free to browse our catalog."
                    
                    st.session_state.chat_history.append({"role": "bot", "text": response})
                    st.rerun()

# ==========================================
#          OWNER DASHBOARD VIEW (Unchanged)
# ==========================================
elif app_mode == "💻 Owner Dashboard":
    st.title("🏪 Aggarwal Store - Partner Dashboard")
    # ... [Owner dashboard logic remains exactly the same as the previous version] ...
    st.info("Switch to 'Customer Storefront' in the sidebar to see the new layout!")
