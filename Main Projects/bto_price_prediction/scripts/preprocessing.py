import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load and clean dataset
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)  # Drop rows with missing values

    # Replace '-' with NaN in target columns and drop invalid rows
    target_columns = [
        'min_selling_price_less_ahg_shg',
        'max_selling_price_less_ahg_shg',
        'min_selling_price',
        'max_selling_price'
    ]
    data[target_columns] = data[target_columns].replace('-', np.nan)

    # Convert to numeric and coerce errors to NaN
    for column in target_columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Drop rows with missing target values
    data.dropna(subset=target_columns, inplace=True)

    # Standardize column names for clarity
    data.rename(columns={
        'min_selling_price': 'min_selling_price_non_sub',
        'max_selling_price': 'max_selling_price_non_sub',
        'min_selling_price_less_ahg_shg': 'min_selling_price_sub',
        'max_selling_price_less_ahg_shg': 'max_selling_price_sub'
    }, inplace=True)

    return data

# Encode categorical data (town and room type)
def encode_data(data):
    # LabelEncoders for category columns
    le_town = LabelEncoder()
    le_room = LabelEncoder()
    
    # Fit and transform 'town' column into numerical value
    data['town_encoded'] = le_town.fit_transform(data['town']) 

    # Fit and transform 'room_type' column into numerical value
    data['room_encoded'] = le_room.fit_transform(data['room_type'])
    
    return data, le_town, le_room

# Split dataset into features (X) and target variables (y)
def split_features_and_targets(data):
    # Feature matrix (X) with categories
    X = data[['financial_year', 'town_encoded', 'room_encoded']]

    # Target variables (y) for subsidized and non-subsidized prices
    y_min_sub = data['min_selling_price_sub']
    y_max_sub = data['max_selling_price_sub']
    y_min_non_sub = data['min_selling_price_non_sub']
    y_max_non_sub = data['max_selling_price_non_sub']
    
    return X, y_min_sub, y_max_sub, y_min_non_sub, y_max_non_sub
