import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV
df = pd.read_csv('expenses.csv')

# --- 修正：數據清洗與分類 ---
# 把分類轉成首字母大寫，避免 'food' 和 'Food' 被當成不同類別
df['category'] = df['category'].str.capitalize()

# 重新進行 Groupby 分類匯總
summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
categories = summary.index
amounts = summary.values

# 設定顏色，這次用 Tab20，顏色比較豐富
colors = plt.cm.tab20(range(len(amounts)))

# 建立畫布
fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')

# 繪製圓餅圖
wedges, texts, autotexts = ax.pie(
    amounts, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    pctdistance=0.85,
    explode=[0.05] * len(amounts),
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# 修正甜甜圈圓心
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# --- 處理 Icon 問題的替代方案 ---
# 既然 Emoji 會變方框，我們手動幫標籤加上簡單的符號，或者乾脆用文字
# 這樣就算在沒有 Emoji 字體的環境也能跑
legend_labels = [f"{cat}: ${amt:.2f}" for cat, amt in zip(categories, amounts)]

ax.legend(
    wedges, 
    legend_labels,
    title="Categories Summary",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

plt.title('Expense Distribution by Category', fontsize=15, fontweight='bold')

# 強制正圓
ax.axis('equal')  
plt.tight_layout()

plt.show()