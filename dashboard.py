import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("retail_sales_dataset.csv", sep="\t")

df["Date"] = pd.to_datetime(df["Date"])

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📊 Retail Sales Analytics")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Dashboard", "About Project"]
)

# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.title("🛍️ Retail Sales & Customer Analysis")

    st.subheader("Welcome to Retail Sales Analytics Dashboard")

    st.write(
        """
        This project analyzes retail sales data to understand
        customer purchasing behaviour, product performance,
        sales trends and demographic patterns.
        """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Sales",
            f"₹{df['Total Amount'].sum():,.0f}"
        )

    with col2:
        st.metric(
            "Total Transactions",
            f"{df['Transaction ID'].nunique():,}"
        )

    with col3:
        st.metric(
            "Quantity Sold",
            f"{df['Quantity'].sum():,}"
        )

    st.markdown("---")

    st.subheader("🎯 Project Objective")

    st.write(
        """
        The main objective of this project is to use Data Analytics
        techniques to identify useful patterns and insights from
        retail sales data.

        The analysis focuses on:

        • Sales performance  
        • Product category performance  
        • Customer behaviour  
        • Gender-wise sales  
        • Age-group analysis  
        • Monthly sales trends
        """
    )


# ==========================================
# DASHBOARD PAGE
# ==========================================

elif page == "Dashboard":

    st.title("📊 Retail Sales Dashboard")

    # KPIs
    total_sales = df["Total Amount"].sum()
    total_quantity = df["Quantity"].sum()
    total_transactions = df["Transaction ID"].nunique()
    average_transaction = df["Total Amount"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Sales", f"₹{total_sales:,.0f}")

    with col2:
        st.metric("Transactions", f"{total_transactions:,}")

    with col3:
        st.metric("Quantity Sold", f"{total_quantity:,}")

    with col4:
        st.metric(
            "Average Transaction",
            f"₹{average_transaction:,.0f}"
        )

    st.markdown("---")

    # ==========================================
    # CATEGORY SALES
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🛍️ Sales by Product Category")

        category_sales = (
            df.groupby("Product Category")["Total Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 4))

        category_sales.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Product Category")
        ax.set_ylabel("Sales")
        ax.set_title("Sales by Product Category")

        st.pyplot(fig)

    # ==========================================
    # GENDER SALES
    # ==========================================

    with col2:

        st.subheader("👥 Sales by Gender")

        gender_sales = (
            df.groupby("Gender")["Total Amount"]
            .sum()
        )

        fig, ax = plt.subplots(figsize=(7, 4))

        gender_sales.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Gender")
        ax.set_ylabel("Sales")
        ax.set_title("Sales by Gender")

        st.pyplot(fig)

    st.markdown("---")

    # ==========================================
    # MONTHLY SALES
    # ==========================================

    st.subheader("📈 Monthly Sales Trend")

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    df["Month"] = df["Date"].dt.month_name()

    monthly_sales = (
        df.groupby("Month", observed=False)["Total Amount"]
        .sum()
        .reindex(month_order)
    )

    fig, ax = plt.subplots(figsize=(12, 5))

    monthly_sales.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Sales Trend")
    ax.grid(True)

    st.pyplot(fig)

    st.markdown("---")

    # ==========================================
    # AGE GROUP ANALYSIS
    # ==========================================

    st.subheader("👤 Sales by Age Group")

    bins = [17, 25, 35, 45, 55, 65]
    labels = ["18-25", "26-35", "36-45", "46-55", "56-65"]

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=bins,
        labels=labels
    )

    age_sales = (
        df.groupby("Age Group", observed=False)["Total Amount"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    age_sales.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Age Group")
    ax.set_ylabel("Sales")
    ax.set_title("Sales by Age Group")

    st.pyplot(fig)


# ==========================================
# ABOUT PROJECT
# ==========================================

elif page == "About Project":

    st.title("ℹ️ About the Project")

    st.header("Retail Sales and Customer Purchase Behaviour Analysis")

    st.write(
        """
        This project focuses on analyzing retail sales data using
        Data Analytics techniques.

        The dataset contains information about customer transactions,
        customer demographics, product categories, quantities,
        prices and total sales amounts.
        """
    )

    st.header("📌 Dataset Information")

    st.write(
        """
        The dataset contains 1,000 retail transactions and 9 main
        attributes related to sales and customers.
        """
    )

    st.header("🛠️ Tools & Technologies")

    st.write(
        """
        • Python  
        • Pandas  
        • NumPy  
        • Matplotlib  
        • Seaborn  
        • Streamlit  
        • Data Analytics
        """
    )

    st.header("🎯 Objectives")

    st.write(
        """
        1. Analyze overall retail sales performance.

        2. Identify the best-performing product categories.

        3. Analyze customer purchasing behaviour.

        4. Compare sales across genders.

        5. Analyze sales across different age groups.

        6. Identify monthly sales trends.

        7. Present important findings through an interactive dashboard.
        """
    )

    st.header("📊 Key Analysis")

    st.write(
        """
        The project includes:

        • Sales KPI analysis  
        • Product category analysis  
        • Gender-wise analysis  
        • Monthly sales trend  
        • Age group analysis  
        • Customer behaviour analysis
        """
    )