import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings("ignore", message="X does not have valid feature names")

__locations = None
__data_columns = None
__model = None

def estimated_price(location, total_sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    global __locations
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Update these paths based on your Windows environment
    with open(r"C:\Users\chaud\bangalore\server\artifacts\columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open(r"C:\Users\chaud\bangalore\server\artifacts\bangalore.pickle", 'rb') as f:
        __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(estimated_price("Vijayanagar Vishveshwarya", 1000, 2, 2))
    print(estimated_price("2nd Stage Nagarbhavi", 1000, 2, 3))
    print(estimated_price("Whitefield", 1000, 3, 2))
