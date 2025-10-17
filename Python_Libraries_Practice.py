# ===============================================
#      Python Libraries Practice Exercises
# ===============================================

#  Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
#  NumPy Exercises
# ------------------------

# Exercise 1: Array 1 to 10
arr = np.arange(1, 11)
print("Array 1-10:", arr)

# Exercise 2: 3x3 zeros matrix
zeros_matrix = np.zeros((3,3))
print("3x3 Zeros Matrix:\n", zeros_matrix)

# Exercise 3: Mean, median, std of array
nums = np.array([4, 8, 15, 16, 23, 42])
print("Mean:", np.mean(nums))
print("Median:", np.median(nums))
print("Standard Deviation:", np.std(nums))

# Exercise 4: 5x5 identity matrix
identity_matrix = np.eye(5)
print("5x5 Identity Matrix:\n", identity_matrix)

# Exercise 5: 10 random integers 1-100
random_nums = np.random.randint(1, 101, 10)
print("Random Integers:", random_nums)

# ------------------------
# 3️⃣ Pandas Exercises
# ------------------------

# Exercise 6: Create a DataFrame
data = {
    "Name": ["Babin", "Sudesh", "Manish", "Sita", "Ram"],
    "Age": [21, 22, 20, 19, 23],
    "City": ["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur", "Kathmandu"]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Exercise 7: Read CSV (uncomment if you have a CSV)
# df_csv = pd.read_csv("data.csv")
# print(df_csv.head())

# Exercise 8: Average age
print("Average Age:", df["Age"].mean())

# Exercise 9: Filter rows where City is Kathmandu
print("Rows with City = Kathmandu:\n", df[df["City"] == "Kathmandu"])

# Exercise 10: Add a Score column with random values 50-100
df["Score"] = np.random.randint(50, 101, df.shape[0])
print("\nDataFrame with Score:\n", df)

# ------------------------
#  Matplotlib Exercises
# ------------------------

# Exercise 11: Line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Exercise 12: Bar chart
countries = ["Nepal", "India", "USA"]
population = [30, 1380, 331]  # in millions
plt.figure()
plt.bar(countries, population, color=['red','green','blue'])
plt.title("Population of Countries")
plt.show()

# Exercise 13: Histogram
plt.figure()
plt.hist(nums, bins=5, color='orange', edgecolor='black')
plt.title("Histogram of Numbers")
plt.show()

# Exercise 14: Pie chart
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
values = [30, 20, 25, 25]
plt.figure()
plt.pie(values, labels=fruits, autopct='%1.1f%%', startangle=90)
plt.title("Fruits Pie Chart")
plt.show()

# ------------------------
# Seaborn Exercises
# ------------------------

# Exercise 15: Load tips dataset
tips = sns.load_dataset('tips')
print("\nTips Dataset Head:\n", tips.head())

# Exercise 16: Scatter plot total_bill vs tip
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

# Exercise 17: Histogram of total_bill
plt.figure()
sns.histplot(tips['total_bill'], bins=10, kde=True)
plt.title("Histogram of Total Bill")
plt.show()

# Exercise 18: Boxplot of tip by day
plt.figure()
sns.boxplot(x='day', y='tip', data=tips)
plt.title("Boxplot of Tip by Day")
plt.show()

# Exercise 19: Heatmap of correlations
plt.figure()
sns.heatmap(tips.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ------------------------
#  Extra Challenge
# ------------------------

# 20: NumPy -> Pandas -> Matplotlib
random_data = np.random.randint(1, 101, 100)
df_random = pd.DataFrame(random_data, columns=["RandomNumbers"])
plt.figure()
plt.plot(df_random["RandomNumbers"])
plt.title("Random Numbers Line Chart")
plt.show()
