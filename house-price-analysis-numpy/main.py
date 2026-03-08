from analysis.analysis import analyze_data
from prediction.predict_price import predict_price

print("------ House Price Data Analysis ------")

analyze_data()

print("\n------ House Price Prediction ------")

predict_price(1600)