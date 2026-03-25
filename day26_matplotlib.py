# Day 26: Matplotlib plots
# plotting line charts, bar plots and scatter plots

import matplotlib.pyplot as plt

# data coordinate arrays
days = [1, 2, 3, 4, 5, 6, 7]
study_hours = [2, 3.5, 1.5, 4, 5, 2.5, 3]

plt.figure(figsize=(6, 4))

# plot coordinates line chart
plt.plot(days, study_hours, marker='o', color='g', linestyle='--', label='Study Hours')

plt.title("Study Hours over Days")
plt.xlabel("Days")
plt.ylabel("Hours Studied")
plt.grid(True)
plt.legend()

plt.savefig("study_plot.png")
plt.close()
print("Saved line plot to 'study_plot.png'")

# exercise 1: sales bar chart
products = ["Laptop", "Mouse", "Keyboard"]
sales = [120, 250, 180]
plt.figure()
plt.bar(products, sales, color='blue')
plt.title("Product Sales")
plt.savefig("sales_bar_chart.png")
plt.close()
print("Saved bar plot to 'sales_bar_chart.png'")

# challenge: coordinates scatter plot
np_x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
np_y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]
plt.figure()
plt.scatter(np_x, np_y, color='red', alpha=0.7)
plt.title("Scatter Plot Example")
plt.savefig("scatter_plot.png")
plt.close()
print("Saved scatter plot to 'scatter_plot.png'")
