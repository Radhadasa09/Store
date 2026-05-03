import streamlit as st
import pandas as pd

# --- Page Configuration (Updated) ---
st.set_page_config(
    page_title="Aggarwal Store - Fast Delivery",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
#      NEW COLORFUL CUSTOM CSS (Vibe Update)
# ==========================================
st.markdown("""
    <style>
    /* Main app background color */
    [data-testid="stAppViewContainer"] {
        background-color: #fffbeb; /* Very light yellow/off-white background */
    }

    /* Target the product cards */
    .product-card {
        border: 1px solid #ffe8cc;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        background-color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s, box-shadow 0.2s; /* Smooth pop effect */
        height: 100%; /* Ensure all cards same height */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    /* Hover effect for cards */
    .product-card:hover {
        transform: translateY(-5px) scale(1.01); /* Subtle lift on hover */
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
        border: 1px solid #8b0000; /* Add "Aggarwal Store" Maroon border on hover */
    }

    /* Style the product image inside the card */
    .product-image {
        height: 120px; /* Force image height Consistency */
        object-fit: contain; /* Don't stretch image, keep perspective */
        margin-bottom: 10px;
    }

    /* Price Text Styling */
    .price-text {
        font-weight: bold;
        color: #8b0000; /* Rich Maroon color for price */
        font-size: 1.2em;
        margin-top: 5px;
        margin-bottom: 10px;
    }

    /* Product Name Styling */
    .product-name {
        font-size: 1.0em;
        font-weight: 500;
        color: #333;
        margin-bottom: 0px;
        height: 40px; /* Keep name space consistent even if text wraps */
        overflow: hidden;
    }

    /* Customize the standard Streamlit "ADD" Button (Blinkit Green Vibe) */
    .stButton>button {
        background-color: #0c831f; /* Forest Green */
        color: white !important;
        border-radius: 6px;
        border: none;
        font-weight: bold;
        width: 100%;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #096a18; /* Darker green on hover */
        color: white !important;
        border: none;
    }

    /* Header Styling */
    h1 {
        color: #8b0000; /* Consistent Maroon header */
        font-family: 'Poppins', sans-serif;
    }
    h3 {
        color: #333;
    }

    /* Customize Sidebar look */
    [data-testid="stSidebar"] {
        background-color: #fcefdc; /* Warm, light accent for sidebar */
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 425.50  # Starting below 500 to show alert

# ==========================================
#   NEW STATIC PRODUCT DATA (Using URLs)
# ==========================================
# NOTE: In a real app, replace these URLs with your own images hosted in GitHub (e.g., ./assets/milk.png)
products = [
    {
        "id": 1, "name": "Amul Taaza Toned Milk (500ml)", "price": 27, "category": "Grocery", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/104618_7-amul-taaza-toned-milk.jpg"
    },
    {
        "id": 2, "name": "Harvest Gold Brown Bread", "price": 40, "category": "Grocery", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/10000003_16-harvest-gold-brown-bread.jpg"
    },
    {
        "id": 3, "name": "Classmate Notebook (Unruled, 172 Pgs)", "price": 50, "category": "Stationery", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/293261_11-classmate-notebook-long-size-unruled-single-line.jpg"
    },
    {
        "id": 4, "name": "Pilot V5 Liquid Ink Pen (Blue)", "price": 60, "category": "Stationery", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/1204094_1-pilot-hi-techpoint-05-v5-pen-blue.jpg"
    },
    {
        "id": 5, "name": "Kwality Wall's Cornetto Double Chocochip", "price": 50, "category": "Ice Creams", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/1212879_1-kwality-walls-cornetto-double-chocolush-frozen-dessert.jpg"
    },
    {
        "id": 6, "name": "Magnum Almond Ice Cream Stick", "price": 90, "category": "Ice Creams", 
        "img_url": "https://www.bigbasket.com/media/uploads/p/l/40003290_4-magnum-almond-ice-cream-stick.jpg"
    }
]

def add_to_cart(item):
    st.session_state.cart.append(item)

# --- Sidebar Navigation (Updated with real name) ---
st.sidebar.markdown("### 🏬 Aggarwal Store Nav")
app_mode = st.sidebar.radio("Choose Interface", ["📱 Customer Storefront", "💻 Owner Dashboard"])
st.sidebar.divider()
st.sidebar.markdown("Gurgaon DLF Phase 3 Branch")

# ==========================================
#        CUSTOMER STOREFRONT VIEW (Updated)
# ==========================================
if app_mode == "📱 Customer Storefront":
    st.title("🏪 Aggarwal Store")
    st.markdown("Delivery in **10 minutes** to your doorstep.")
    st.divider()

    # Search Bar
    search = st.text_input("Search for groceries, stationery, and ice creams...", placeholder="Search 'Milk'")

    # Layout: Products on Left (3 columns), Cart on Right (1 column)
    prod_col, cart_col = st.columns([3, 1])

    with prod_col:
        st.subheader("Explore Categories")
        tabs = st.tabs(["All Items", "Grocery", "Stationery", "Ice Creams"])
        
        # Display All Items (the principle applies to filtering categories too)
        with tabs[0]:
            cols = st.columns(3)
            # Use a robust loop that uses container height
            for index, product in enumerate(products):
                with cols[index % 3]:
                    # NEW HTML CARD: Includes Image URL and Name height lock
                    st.markdown(f"""
                        <div class="product-card">
                            <img src='{product['img_url']}' class='product-image' />
                            <p class='product-name'>{product['name']}</p>
                            <p class="price-text">₹{product['price']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.button("ADD", key=f"add_{product['id']}", on_click=add_to_cart, args=(product,), use_container_width=True)

    # --- Floating Cart Column (Unchanged Logic, basic styling update) ---
    with cart_col:
        st.markdown("### 🛒 Your Cart")
        if not st.session_state.cart:
            st.info("Your cart is empty. Tap 'ADD' to get started!")
        else:
            cart_df = pd.DataFrame(st.session_state.cart)
            cart_summary = cart_df.groupby(['name', 'price']).size().reset_index(name='qty')
            cart_summary['total'] = cart_summary['price'] * cart_summary['qty']
            
            # Display items
            for _, row in cart_summary.iterrows():
                st.write(f"**{row['qty']}x** {row['name']} - **₹{row['total']}**")
            
            st.divider()
            subtotal = cart_summary['total'].sum()
            
            # Delivery Fee Logic
            delivery_fee = 0 if subtotal >= 250 else 30
            st.write(f"**Subtotal:** ₹{subtotal}")
            if delivery_fee == 0:
                st.success("Delivery Fee: FREE (Order above ₹250)")
            else:
                st.warning(f"Delivery Fee: ₹{delivery_fee} (Add ₹{250-subtotal} more for free delivery)")
            
            st.write(f"### **Total: ₹{subtotal + delivery_fee}**")
            st.button("Checkout & Pay (UPI/Khata)", type="primary", use_container_width=True)

# ==========================================
#          OWNER DASHBOARD VIEW (Unchanged Logic)
# ==========================================
elif app_mode == "💻 Owner Dashboard":
    st.title("🏪 Aggarwal Store - Partner Dashboard")

    # Low Wallet Alert
    if st.session_state.wallet_balance < 500:
        st.error(f"⚠️ **Low Wallet Balance (₹{st.session_state.wallet_balance:.2f})**: Please recharge your platform wallet to keep accepting Home Delivery orders.")

    # --- Executive KPIs ---
    st.markdown("### Today's Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Today's Sales", value="₹4,250", delta="+₹450")
    with col2:
        st.metric(label="Pending Deliveries", value="4", delta="-1")
    with col3:
        st.metric(label="Total Outstanding Khata", value="₹12,500", delta="-₹200", delta_color="inverse")
    with col4:
        st.metric(label="Platform Wallet Balance", value=f"₹{st.session_state.wallet_balance:.2f}")

    st.divider()

    # --- Navigation Tabs ---
    tab1, tab2, tab3 = st.tabs(["📦 Active Orders", "📖 Khata Ledger", "💳 Wallet & Billing"])

    with tab1:
        st.subheader("Live Delivery Orders")
        orders = pd.DataFrame({
            "Order ID": ["#1042", "#1043", "#1044"],
            "Customer": ["Rahul M.", "Priya S.", "Amit K."],
            "Items": ["Milk, Bread, Eggs", "Stationery Kit", "Ice Cream Family Pack"],
            "Amount": ["₹280", "₹150", "₹320"],
            "Status": ["Packing", "Ready", "Out for Delivery"]
        })
        st.dataframe(orders, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Digital Khata (Credit Customers)")
        khata_data = pd.DataFrame({
            "Customer": ["Vikram Singh", "Neha Gupta", "Aman Verma"],
            "Phone": ["+91-9876543210", "+91-9876543211", "+91-9876543212"],
            "Outstanding": ["₹4,500", "₹1,200", "₹6,800"],
            "Last Paid": ["12 Days Ago", "5 Days Ago", "30 Days Ago"]
        })
        st.dataframe(khata_data, use_container_width=True, hide_index=True)
        st.button("Remind All via WhatsApp", icon="💬")

    with tab3:
        st.subheader("Platform Wallet History")
        st.info("**Pricing Tier Active:** 3% fee on Home Deliveries | 1% fee on pure Khata settlements.")
        
        col_wallet1, col_wallet2 = st.columns([2, 1])
        with col_wallet1:
            st.markdown("**Recent Deductions**")
            ledger_data = pd.DataFrame({
                "Date/Time": ["Today, 2:30 PM", "Today, 1:15 PM", "Yesterday, 8:00 PM"],
                "Transaction Type": ["Home Delivery (#1042)", "Khata Settlement", "Home Delivery (#1041)"],
                "Order Value": ["₹280.00", "₹1,500.00", "₹450.00"],
                "Fee Applied": ["3%", "1%", "3%"],
                "Wallet Deduction": ["-₹8.40", "-₹15.00", "-₹13.50"]
            })
            st.dataframe(ledger_data, use_container_width=True, hide_index=True)

        with col_wallet2:
            st.markdown("**Recharge Wallet**")
            st.write(f"Current Balance: **₹{st.session_state.wallet_balance:.2f}**")
            # Generate QR code pointing to real owner's UPI
            st.image(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=yourplatform@upi&pn=AggarwalStore", width=150)
            st.write("*Scan to add ₹1,000 via UPI*")
            if st.button("Simulate Recharge", type="primary", use_container_width=True):
                st.session_state.wallet_balance += 1000
                st.rerun()
