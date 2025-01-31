import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Black Friday Sale Data Analysis", layout="wide")

# Add a background image (optional for a more dynamic look)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/asfalt.png");
    }
    </style>
    """, unsafe_allow_html=True
)

# Load the data
df = pd.read_csv('BlackFriday.csv')

# Sidebar for navigation
st.sidebar.title("Navigation")
menu = ["Home", "Data Overview", "Gender & Age Analysis", "Purchase Analysis", "City & Occupation Analysis"]
choice = st.sidebar.radio("Go to", menu)

# Home Page
if choice == "Home":
    st.title("🛍️ Black Friday Sale Data Analysis")
    st.markdown("""
        Welcome to the **Black Friday Sale Data Analysis** app! 🛒
        
        Use the navigation on the left to explore various insights from the dataset.
    """)

# Data Overview
elif choice == "Data Overview":
    st.title("📊 Data Overview")
    st.subheader("Raw Data")
    st.dataframe(df, width=800, height=400)

    # Data Information
    st.subheader("ℹ️ Data Information")
    st.write(df.info())

    # Check for Null Values
    st.subheader("🔎 Null Values")
    st.write(df.isnull().sum())

    # Drop Null Values
    df_cleaned = df.dropna()
    st.subheader("✅ Data After Dropping Null Values")
    st.write(df_cleaned)

    # Drop 'Product_Category_2' & 'Product_Category_3'
    df_cleaned.drop(columns=["Product_Category_2", "Product_Category_3"], inplace=True)
    st.subheader("❌ Data After Dropping Product Categories 2 and 3")
    st.write(df_cleaned)

    # Unique Value Counts and Distribution
    st.subheader("🔢 Unique Values and Distribution")
    for column in df.columns:
        st.write(f"**{column}:** {df[column].nunique()} unique values")

# Gender & Age Analysis
elif choice == "Gender & Age Analysis":
    st.title("👩‍🦱👨‍🦰 Gender & Age Analysis")

    # Gender Distribution (Pie Chart & Countplot)
    st.subheader("Gender Distribution")
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(6, 6))
        df.groupby('Gender').size().plot(kind='pie', autopct='%.1f%%', ax=ax, colors=["#ff9999", "#66b3ff"])
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.countplot(x="Age", hue="Gender", data=df, palette="coolwarm", ax=ax)
        st.pyplot(fig)

    # Age Distribution (Bar Chart)
    st.subheader("🛍️ Purchase Distribution by Age")
    fig, ax = plt.subplots(figsize=(12, 6))
    df.groupby('Age').size().plot(kind='bar', title='Purchase Distribution By Age', color='#5cb85c', ax=ax)
    st.pyplot(fig)

    # Unique Products Purchased by Age
    st.subheader("🧑‍💻 Unique Products Purchased by Age")
    lst = [[age, df[df["Age"] == age]['Product_ID'].nunique()] for age in df['Age'].unique()]
    age_product_data = pd.DataFrame(lst, columns=['Age', 'Products'])
    st.write(age_product_data)

    # Bar Chart for Unique Products by Age
    st.subheader("📦 Unique Products Purchased by Age - Bar Chart")
    fig, ax = plt.subplots(figsize=(10, 5))
    age_product_data.plot.bar(x='Age', ax=ax, color="#ffcc00")
    st.pyplot(fig)

# Purchase Analysis
elif choice == "Purchase Analysis":
    st.title("💰 Purchase Analysis")

    # Amount Spent by Age (Bar Chart)
    st.subheader("💸 Amount Spent by Age")
    fig, ax = plt.subplots(figsize=(12, 6))
    df.groupby('Age').sum()['Purchase'].plot(kind='bar', title='Amount Spent by Age', color='#ff6600', ax=ax)
    st.pyplot(fig)

    # Marital Status Distribution (Pie Chart)
    st.subheader("💍 Marital Status Distribution")
    fig, ax = plt.subplots(figsize=(6, 6))
    df.groupby('Marital_Status').size().plot(kind='pie', autopct='%0.1f%%', ax=ax, colors=["#ff6347", "#32cd32"])
    st.pyplot(fig)

    # Total Purchase by Product Category 1 (Bar Chart)
    st.subheader("💸 Total Purchase by Product Category 1")
    fig, ax = plt.subplots(figsize=(6, 6))
    df.groupby('Product_Category_1').sum()['Purchase'].sort_values().plot(kind='bar', ax=ax, color="#ffcc00")
    st.pyplot(fig)

# City & Occupation Analysis
elif choice == "City & Occupation Analysis":
    st.title("🏙️ City & Occupation Analysis")

    # City Category Distribution (Countplot)
    st.subheader("🏙️ City Category Distribution")
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.countplot(x=df['City_Category'], ax=ax, palette="Blues")
    st.pyplot(fig)

    # Stay in Current City Years Distribution (Countplot & Pie Chart)
    st.subheader("📅 Stay in Current City Years Distribution")
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.countplot(x=df['Stay_In_Current_City_Years'], ax=ax, palette="viridis")
    st.pyplot(fig)

    st.subheader("🏠 Stay in Current City Years - Pie Chart")
    fig, ax = plt.subplots(figsize=(6, 6))
    df.groupby('Stay_In_Current_City_Years').size().plot(kind='pie', autopct="%.1f%%", ax=ax, colors=["#ffcccc", "#c2c2f0", "#ffb3e6"])
    st.pyplot(fig)

    # Occupation Analysis (Countplot & Bar Chart)
    st.subheader("💼 Occupation Distribution")
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.countplot(x=df['Occupation'], ax=ax, palette="coolwarm")
    st.pyplot(fig)

    st.subheader("🔢 Count of Each Occupation")
    fig, ax = plt.subplots(figsize=(6, 6))
    df.groupby('Occupation').size().sort_values().plot(kind='bar', ax=ax, color="#66cc66")
    st.pyplot(fig)

    st.subheader("💸 Total Purchase by Occupation")
    fig, ax = plt.subplots(figsize=(6, 6))
    df.groupby('Occupation').sum()['Purchase'].sort_values().plot(kind='bar', ax=ax, color="#ff6600")
    st.pyplot(fig)

