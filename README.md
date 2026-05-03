# 🏪 Digital Dukaan: Hyper-Local Grocery & Khata Platform

A dual-interface, hyper-local commerce platform designed to bridge the gap between neighborhood retail shops (Dukaans) and modern quick-commerce convenience. It combines a "Blinkit-style" customer storefront with a robust, zero-leak operational dashboard for shop owners.

## 🚀 Project Overview

Local grocery shops often operate on thin margins and rely heavily on traditional, paper-based monthly credit (Khata) systems. This project digitizes that relationship, allowing customers to order online for quick delivery while giving shop owners a modern tool to track inventory, manage outstanding credit, and process UPI payments seamlessly.

### Core Business Model (Tiered Commission)
*   **3% Platform Fee:** Applied to new Home Delivery orders.
*   **1% Platform Fee:** Applied to pure Khata (credit) settlements and walk-in digital management.
*   **Prepaid Wallet:** Owners maintain a prepaid platform wallet from which micro-commissions are auto-deducted, ensuring zero revenue leakage.

## ✨ Key Features

**For the Shop Owner (Streamlit Dashboard)**
*   **Live Order Management:** Real-time tracking of incoming delivery orders.
*   **Digital Khata Ledger:** Track outstanding customer credit with one-click WhatsApp reminders.
*   **Wallet & Billing Transparency:** A clear, ledger-style view of platform commission deductions.
*   **Low Balance Alerts:** Automated UI warnings when the prepaid wallet drops below ₹500.

**For the Customer (Frontend App)**
*   **Blinkit-Style UI:** A clean, mobile-first product grid organized by categories (Grocery, Stationery, Ice Creams).
*   **Passwordless Login:** OTP-based authentication that remembers the user's device for frictionless return visits.
*   **Hybrid Checkout:** Pay immediately via UPI Intent (GPay/PhonePe) or "Pay Later" (added to monthly Khata).
*   **Smart Cart Logic:** Free delivery automatically applied for orders exceeding ₹250.

## 🛠️ Tech Stack

*   **Frontend (Owner Dashboard):** Python, Streamlit, Pandas
*   **Backend & Database:** Supabase (PostgreSQL)
*   **Authentication:** Supabase Auth (OTP / Passwordless)
*   **Data Visualization:** Streamlit Native Metrics and Dataframes

## 📂 Project Structure
```text
digital_dukaan/
├── app.py                 # Main Streamlit execution file
├── pages/                 # Multipage app directory (if applicable)
│   ├── 01_dashboard.py
│   ├── 02_inventory.py
├── components/            # Reusable UI components (Product cards, alerts)
├── database/              # Supabase connection handlers and CRUD logic
├── assets/                # Images, icons, and custom CSS
├── requirements.txt       # Python dependencies
└── README.md
