import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV
df = pd.read_csv('expenses.csv')


amounts = df['amount']
categories = df['category']

# 設定顏色
colors = plt.cm.get_cmap('Pastel2')(range(len(amounts)))

fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')


wedges, texts, autotexts = ax.pie(
    amounts, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    pctdistance=0.82,
    explode=[0.05] * len(amounts),
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)


centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)


legend_labels = [f"{cat} (${amt})" for i, (cat, amt) in enumerate(zip(categories, amounts))]

ax.legend(
    wedges, 
    legend_labels,
    title="Expense Details",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1) 
)

plt.title('Individual Expense Breakdown', fontsize=15, fontweight='bold')

# 強制正圓
ax.axis('equal')  
plt.tight_layout()

plt.show()
