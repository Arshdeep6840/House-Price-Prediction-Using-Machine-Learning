import pandas as pd
import streamlit as st
import numpy as np
import re
import joblib
from babel.numbers import format_decimal
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Home Page", page_icon="🏠", layout="wide")
df = pd.read_csv(r'D:\Data science\LLM-LangChain\99 houses\data\final_df.csv')



st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home","Analysis", "Predict", "About"])
if page == "Home":

    # ✅ Example loader: FROM URL
    def load_lottie_url(url: str):
        r = requests.get(url)
        print("Status Code:", r.status_code)
        if r.status_code != 200:
            print("Response:", r.text)
            return None
        return r.json()



    lottie_home = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_q5pk6p1k.json")

    # Debug: check if loaded
    print(lottie_home)

    # Page title
    st.title("🏠 Welcome to the Home Page")
    st.write(
        """
        This is an example Streamlit Home Page with a simple Lottie animation.
        Lottie animations make your page look modern and lively!
        """
    )


    col1, col2 = st.columns(2)

    with col1:
        if lottie_home is not None:
            st_lottie(lottie_home, speed=1, height=300, key="home")
        else:
            st.error("Failed to load Lottie animation.")

    with col2:
        st.header("Why use Lottie?")
        st.write(
            """
            - 🎉 Easy to add  
            - ✨ Looks professional  
            - 🌐 Works on all devices
            """
        )
        st.button("Click me!")
elif page == "Analysis":

    st.title("🏡 99 Houses - Data Analysis")
    st.write("Exploring key features of the housing dataset")

    # Show data preview
    with st.expander("🔍 Show Data"):
        st.dataframe(df[[
            'log_area', 'bed_bath_ratio', 'additional_room_count',
            'adjusted_price_per_sqft', 'balcony', 'bathroom', 'bedRoom',
            'features_score', 'floor', 'furnish_score'
        ]].head())

    # Show summary statistics
    st.header("📊 Summary Statistics")
    st.write(df[[
            'log_area', 'bed_bath_ratio', 'additional_room_count',
            'adjusted_price_per_sqft', 'balcony', 'bathroom', 'bedRoom',
            'features_score', 'floor', 'furnish_score'
        ]].describe())

    # Correlation heatmap
    st.header("🔗 Correlation Heatmap")

    num_cols = [
        'log_area', 'bed_bath_ratio', 'additional_room_count',
        'adjusted_price_per_sqft', 'bathroom', 'bedRoom',
        'features_score', 'floor', 'furnish_score'
    ]

    corr = df[num_cols].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Sidebar for custom plots
    st.sidebar.header("📌 Custom Plots")

    col_option = st.sidebar.selectbox(
        "Select a numerical column",
        num_cols
    )

    st.header(f"📈 Distribution of {col_option}")

    fig2, ax2 = plt.subplots()
    sns.histplot(df[col_option], kde=True, ax=ax2)
    st.pyplot(fig2)

    # Scatter plot for relation between two features
    x_option = st.sidebar.selectbox("X-axis", num_cols, index=0)
    y_option = st.sidebar.selectbox("Y-axis", num_cols, index=1)

    st.header(f"⚡ Scatter Plot: {x_option} vs {y_option}")

    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x=x_option, y=y_option, hue='sector', ax=ax3)
    st.pyplot(fig3)

    # Categorical columns: sector, society_clean, property_name
    st.header("🏘️ Top Sectors & Societies")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sectors")
        sector_counts = df['sector'].value_counts().head(10)
        st.bar_chart(sector_counts)

    with col2:
        st.subheader("Societies")
        society_counts = df['society_clean'].value_counts().head(10)
        st.bar_chart(society_counts)

    st.success("✅ EDA Completed")


elif page == "Predict":
    st.title("🏠 Flat/House of Gurgaon Price Prediction")
    with st.expander("🎯 **Instructions**"):
        st.write( """
        - Enter the property details below.
        - Click **Predict** to see the estimated flat/house price.
        - Review the result carefully.
       """)

    property_names = df['property_name'].unique()

    additional_room_count = ['0', '1', '2', '3', '4']
    bedroom_count = ['1', '2', '3', '4', '5', '6']
    bathroom_count = ['1', '2', '3', '4', '5', '6', '7']
    balcony_count = ['1', '2', '3', '3+', 'No']
    bed_bath_ratio = []
    log_area = []

    sector_society_map = df.groupby('sector')['society_clean'].unique().to_dict()


    st.header("Input Property Details")
    # Create two columns
    col1, col2 = st.columns(2)

    # Add stuff in the first column
    with col1:
        property_name = st.selectbox("Property Name", property_names)
        sectors = st.selectbox("Select Sector", sorted(sector_society_map.keys()))
        related_societies = sorted(sector_society_map[sectors])
        societies = st.selectbox("Select Society", related_societies)
        bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=7, value=2, step=1)
        balcony = st.selectbox("Number of Balconies", balcony_count)
        floor = st.number_input("Floor Number", min_value=0, max_value=45, value=1, step=1)


    # Add stuff in the second column
    with col2:
        SuperBuildUp_adjusted_area = st.number_input("Super BuildUp Area", min_value=1000.0,max_value=868480.0, value=1200.0,step=10.0)
        adjusted_price_per_sqft = st.number_input("Price per sqft", min_value=500.0, max_value=181818.0, value=5000.0, step=50.0)
        furnish_score = st.number_input("Furnish Score", min_value=1, value=5, step=1, max_value=20)
        features_score = st.number_input("Features Score", min_value=0, value=20, step=1, max_value=50)
        rating_sum = st.number_input("Rating", min_value=0.0, value=10.0)
        additional_room_count = st.selectbox("Additional Room", ['0', '1', '2', '3', '4'])

    # Load your model (should be VotingRegressor or Pipeline)
    model = joblib.load(r"D:\Data science\LLM-LangChain\99 houses\Model\flat_price_prediction.pkl")
    # Fix: handle single property_name string
    def extract_bhk_number(single_bhk_string):
        match = re.search(r'\d+', single_bhk_string)
        if match:
            return int(match.group())
        return None
    bedRoom = extract_bhk_number(property_name)

    bed_bath_ratio = bedRoom / bathroom if bathroom != 0 else 0
    log_area = np.log1p(SuperBuildUp_adjusted_area)

    user_input = [
        log_area,
        bed_bath_ratio,
        int(additional_room_count),
        adjusted_price_per_sqft,
        balcony,
        bathroom,
        bedRoom,
        features_score,
        floor,
        furnish_score,
        sectors,
        societies,
        property_name,
    ]

    columns = ['log_area', 'bed_bath_ratio', 'additional_room_count',
               'adjusted_price_per_sqft', 'balcony', 'bathroom', 'bedRoom',
               'features_score', 'floor', 'furnish_score', 'sector', 'society_clean',
               'property_name']
    input_array = pd.DataFrame([user_input], columns=columns)

    if st.button("Predict"):
        prediction = model.predict(input_array)[0]
        log_reverse = np.expm1(prediction)
        if log_reverse < 0:
            log_reverse = log_reverse * 1_000_000
        else:
            log_reverse = log_reverse * 1_00_00_000

        # Always take absolute, if needed
        log_reverse = abs(log_reverse)

        # Format in Indian style
        formatted = format_decimal(log_reverse, locale='en_IN')

        # Display
        st.success(f"✅ **Predicted Price:** ₹{formatted}")

    with st.expander("⚠️ **Disclaimer**"):
        st.write( """
        - 📌 *This tool uses a machine learning model trained on historical data.*
        - 💡 *The predicted price is an estimate only and may not reflect real-time market conditions.*
        - 🏡 *Always verify with certified real estate professionals before making investment decisions.*
        - ✅ *We do not guarantee accuracy or accept liability for any financial loss.*
        """)


elif page == "About":
    st.title("ℹ️ About Page")
    st.write("About this app...")







