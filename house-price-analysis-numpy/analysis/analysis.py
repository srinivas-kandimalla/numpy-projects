import numpy as np
from data.house_data import sizes, prices

def analyze_data():

    print("House Sizes:", sizes)
    print("House Prices:", prices)

    print("Average Size:", np.mean(sizes))
    print("Average Price:", np.mean(prices))

    print("Highest Price:", np.max(prices))
    print("Lowest Price:", np.min(prices))

    price_per_sqft = prices / sizes

    print("Price per sqft:", price_per_sqft)

    return price_per_sqft