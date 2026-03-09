import numpy as np

# Monthly sales data for 5 products
sales = np.array([120, 150, 100, 180, 90])

print("Sales Data:", sales)

# Total sales
total_sales = np.sum(sales)
print("Total Sales:", total_sales)

# Average sales
average_sales = np.mean(sales)
print("Average Sales:", average_sales)

# Highest sales
max_sales = np.max(sales)
print("Highest Sales:", max_sales)

# Lowest sales
min_sales = np.min(sales)
print("Lowest Sales:", min_sales)

# Best selling product index
best_product = np.argmax(sales)
print("Best Selling Product Index:", best_product)