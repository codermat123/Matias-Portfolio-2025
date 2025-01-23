import streamlit as st
from scripts.preprocessing import load_and_clean_data, encode_data, split_features_and_targets
from scripts.recommendations import recommend_bto_budget
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
import plotly.graph_objects as go


# loading and preprocessing data
data = load_and_clean_data("data/bto_data.csv")
data['room_type'] = data['room_type'].str.strip().str.lower()
data = data[data['room_type'] != '2-room']  # Exclude 2-room flats
data['room_type'] = data['room_type'].replace({'two-room': '2-room', '2-room': '2-room'})  # adjusting based on dataset
data, le_town, le_room = encode_data(data)
X, y_min_sub, y_max_sub, y_min_non_sub, y_max_non_sub = split_features_and_targets(data)

# Polynomial Regression setup
degree = 2
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

# Training the models
min_model_sub = LinearRegression().fit(X_poly, y_min_sub)
max_model_sub = LinearRegression().fit(X_poly, y_max_sub)
min_model_non_sub = LinearRegression().fit(X_poly, y_min_non_sub)
max_model_non_sub = LinearRegression().fit(X_poly, y_max_non_sub)

# Streamlit App
st.title("BTO Price Prediction App")

# Note for developer
st.markdown("<p style='font-size:18px; color:gray;'>Developed by Matias Fong</p>", unsafe_allow_html=True)

# Note for disclaimer
st.markdown(
    "<h3 style='font-size:20px; color:gray;'>⚠️ Developer's Note: Predictions use Polynomial Regression (degree=2), "
    "assuming STEADY non-linear market trend without accounting for abrupt market movements. "
    "Use Predictions as a guide only.</h3>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='font-size:25px;'>🛠️Use the left sidebar to toggle between different features and preferences.</p>",
    unsafe_allow_html=True
)

# Initializing sessions when in default
if "view_historical" not in st.session_state:
    st.session_state["view_historical"] = True

if "view_prediction" not in st.session_state:
    st.session_state["view_prediction"] = False

if "view_budget" not in st.session_state:
    st.session_state["view_budget"] = False

# Sidebar Buttons for Mode Switching
with st.sidebar:
    st.subheader("Mode Selection")
    if st.button("Historical Data only"):
        st.session_state["view_historical"] = True
        st.session_state["view_budget"] = False
        st.session_state["view_prediction"] = False
    if st.button("Price Prediction Mode"):
        st.session_state["view_historical"] = False
        st.session_state["view_budget"] = False
        st.session_state["view_prediction"] = True
    if st.button("Find Your Ideal BTO Based on Budget"):
        st.session_state["view_budget"] = True
        st.session_state["view_historical"] = False
        st.session_state["view_prediction"] = False

# Plot cart for Historical and Prediction Modes
def plot_chart(data, future_year, location, room_type, subsidized, predicted_min=None, predicted_max=None):
    subsidy_label = "Subsidized" if subsidized == "Yes" else "Non-Subsidized"

    if subsidized == "Yes":
        historical = data[(data['town'] == location) & (data['room_type'] == room_type)][
            ['financial_year', 'min_selling_price_sub', 'max_selling_price_sub']
        ]
        historical.rename(
            columns={
                'min_selling_price_sub': 'min_selling_price',
                'max_selling_price_sub': 'max_selling_price'
            }, 
            inplace=True
        )
    else:
        historical = data[(data['town'] == location) & (data['room_type'] == room_type)][
            ['financial_year', 'min_selling_price_non_sub', 'max_selling_price_non_sub']
        ]
        historical.rename(
            columns={
                'min_selling_price_non_sub': 'min_selling_price',
                'max_selling_price_non_sub': 'max_selling_price'
            }, 
            inplace=True
        )

    historical = historical[(historical['min_selling_price'] > 0) & (historical['max_selling_price'] > 0)]
    if not historical.empty:
        historical['financial_year'] = historical['financial_year'] % 100  # Get the last two digits of the year

    future_year_two_digit = future_year % 100  # Convert future year to two-digit format

    fig = go.Figure()

    if not historical.empty:
        fig.add_trace(go.Scatter(
            x=historical['financial_year'],
            y=historical['min_selling_price'],
            mode='lines+markers',
            name="Historical Min"
        ))
        fig.add_trace(go.Scatter(
            x=historical['financial_year'],
            y=historical['max_selling_price'],
            mode='lines+markers',
            name="Historical Max"
        ))

    if predicted_min is not None and predicted_max is not None:
        fig.add_trace(go.Scatter(
            x=[future_year_two_digit],
            y=[predicted_min],
            mode='markers',
            name="Predicted Min",
            marker=dict(color='green', size=10, symbol='circle')
        ))
        fig.add_trace(go.Scatter(
            x=[future_year_two_digit],
            y=[predicted_max],
            mode='markers',
            name="Predicted Max",
            marker=dict(color='red', size=10, symbol='circle')
        ))

    min_year = historical['financial_year'].min() if not historical.empty else 0
    max_year = future_year_two_digit + 1
    fig.update_xaxes(
        range=[min_year - 1, max_year],
        title="Year (20XX)", 
        tickmode="linear",
        dtick=1,
        showgrid=True
    )

    fig.update_layout(
    title=f"{room_type} Prices in {location} ({subsidy_label}) - Chart",
    title_font=dict(size=24),  # Adjust this size value to make the title larger
    yaxis_title="Price ($)",
    hovermode="x unified",
    showlegend=True,
)

    st.plotly_chart(fig)

# Historical Data only session
if st.session_state["view_historical"]:
    st.markdown("<h2 style='font-size:30px;'>⏳Historical Data only view</h2>", unsafe_allow_html=True)
    location = st.sidebar.selectbox("🌎Select Location", sorted(data['town'].unique()))
    room_type = st.sidebar.selectbox("🏠Select Room Type", sorted(data['room_type'].unique()))
    subsidized = st.sidebar.radio("💰Subsidized Prices? (AHG & SHG Grant)", ["Yes", "No"])

    plot_chart(data, 2023, location, room_type, subsidized)  # Show historical chart only

# Prediction Mode session
if st.session_state["view_prediction"]:
    st.sidebar.header("User Inputs")

    years_from_now = st.sidebar.slider("⏰Years from 2023", 3, 15, 5)
    future_year = 2023 + years_from_now
    location = st.sidebar.selectbox("🌎Select Location", sorted(data['town'].unique()))
    room_type = st.sidebar.selectbox("🏠Select Room Type", sorted(data['room_type'].unique()))
    subsidized = st.sidebar.radio("💰Subsidized Prices? (AHG & SHG Grant)", ["Yes", "No"])
    scaling_factor = st.sidebar.slider("📈Market Strength Scaling (Weak < 1 < Strong)", 0.5, 2.0, 1.0, step=0.1)

    def predict_price(min_model, max_model, year, town, room, scaling):
        # Encode input features using labelEncoder, converts categorical to numerical
        town_encoded = le_town.transform([town])[0]
        room_encoded = le_room.transform([room])[0]
        input_data = pd.DataFrame([[year, town_encoded, room_encoded]], 
                                columns=['financial_year', 'town_encoded', 'room_encoded'])
        input_poly = poly.transform(input_data)

        # Predict and scale the min and max prices
        scaled_min_price = int(min_model.predict(input_poly)[0] * scaling)
        scaled_max_price = int(max_model.predict(input_poly)[0] * scaling)

        # Narrow down predicted range
        narrowing_factor = 0.5
        midpoint = (scaled_min_price + scaled_max_price) / 2
        narrowed_min_price = midpoint - (midpoint - scaled_min_price) * narrowing_factor
        narrowed_max_price = midpoint + (scaled_max_price - midpoint) * narrowing_factor

        # Return the narrowed price range
        return int(narrowed_min_price), int(narrowed_max_price)

    #Predict sub / non-sub values
    if subsidized == "Yes":
        predicted_min, predicted_max = predict_price(
            min_model_sub, max_model_sub, future_year, location, room_type, scaling_factor
        )
        subsidy_status = "Subsidized"
    else:
        predicted_min, predicted_max = predict_price(
            min_model_non_sub, max_model_non_sub, future_year, location, room_type, scaling_factor
        )
        subsidy_status = "Non-Subsidized"


    # Find the most recent price data for the selected town and room type
    most_recent_data = data[(data['town'] == location) & (data['room_type'] == room_type)]
    most_recent_data = most_recent_data[most_recent_data['financial_year'] == most_recent_data['financial_year'].max()]

    if subsidized == "Yes":
        recent_min_price = most_recent_data['min_selling_price_sub'].values[0]
        recent_max_price = most_recent_data['max_selling_price_sub'].values[0]
    else:
        recent_min_price = most_recent_data['min_selling_price_non_sub'].values[0]
        recent_max_price = most_recent_data['max_selling_price_non_sub'].values[0]

    # Get the year of the latest data
    latest_data_year = most_recent_data['financial_year'].max()

    # Calculate the percentage change in price
    def calculate_percentage_change(predicted, recent):
        return ((predicted - recent) / recent) * 100 if recent != 0 else 0

    min_percentage_change = calculate_percentage_change(predicted_min, recent_min_price)
    max_percentage_change = calculate_percentage_change(predicted_max, recent_max_price)

    # Subheader and predicted price range
    st.subheader(
        f"🟢Predicted Price Range for {future_year} - {room_type.title()} in {location.title()} ({subsidy_status})"
    )

    # Display predicted price range 
    st.markdown(
        f"<p style='font-size:25px;'><strong><span style='color: orange;'>${predicted_min:,}</span> - "
        f"<span style='color: orange;'>${predicted_max:,}</span></strong></p>",
        unsafe_allow_html=True
    )

    # Display percentage change for Min and Max price
    st.markdown(
        f"<h3 style='font-size:22px;'>🔴 Percentage Change from Latest Data as of {latest_data_year}:</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='font-size:20px;'>Min Price Change: {min_percentage_change:.2f}%</p>", 
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='font-size:20px;'>Max Price Change: {max_percentage_change:.2f}%</p>", 
        unsafe_allow_html=True
    )

    # Plot chart
    plot_chart(data, future_year, location, room_type, subsidized, predicted_min, predicted_max)

# BTO Recommender session
if st.session_state["view_budget"]:
    st.title("Find your Ideal BTO:")

    # Year selection for BTO application (2026–2038) with placeholder "Select here"
    year_selected = st.selectbox("When do you plan to apply for BTO?", 
                                 ["Select here", *list(range(2026, 2039))], index=0)  
    
    # Budget selection, commas, formatted numbers and placeholder "Select here"
    budget_value = st.selectbox(
        "What is your budget?", 
        ["Select here"] + [f"{x:,}" for x in range(400000, 1000001, 200000)],
        index=0  # Default to "Select here"
    )

    # Region selection with placeholder "Select here"
    region = st.selectbox("Select Region", ["Select here", "West", "North", "North-East"], index=0)  # Default to "Select here"

    # Display user selections 
    if year_selected != "Select here" and budget_value != "Select here" and region != "Select here":
        st.subheader("Your Selections:")
        st.write(f"BTO Application Year: {year_selected}")
        st.write(f"Budget: {budget_value}")
        st.write(f"Region: {region}")

        # Call the recommendation function
        recommended_flat = recommend_bto_budget(str(year_selected), region, int(budget_value.replace(',', '')))

        # Display the recommendation 
        if isinstance(recommended_flat, dict):
            st.subheader("✅Based on our prediction, the best option for you is:")
            st.markdown(
                f"<h2 style='color: orange;'>{recommended_flat['room_type']} flat, {recommended_flat['town']}</h2>", 
                unsafe_allow_html=True
            )
        else:
            st.write(recommended_flat)  # If no recommendation
    else:
        st.write("Please select all the fields to get a recommendation.")

# Placeholder for download button
download_placeholder = st.empty()

#Download dataset button
download_placeholder.download_button(
    label="Download Dataset",  # Button label
    data=data.to_csv(index=False),  # Data to download (CSV format)
    file_name="bto_data.csv",  # The file name when downloading
    mime="text/csv",  # MIME type for CSV file
)

