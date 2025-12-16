import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV
df = pd.read_csv('expenses.csv')

# 假設 amount 是數字
expense_summary = df.groupby('category')['amount'].sum()

# 圓餅圖資料
labels = expense_summary.index
sizes = expense_summary.values

# 繪製圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Expense Distribution by Category')
plt.axis('equal') 

plt.show()