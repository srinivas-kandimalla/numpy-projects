import numpy as np
from data.house_data import sizes, prices

def predict_price(size):

    price_per_sqft = prices / sizes
    avg_price_per_sqft = np.mean(price_per_sqft)

    predicted_price = avg_price_per_sqft * size

    print("Predicted price for", size, "sqft house:", predicted_price)