import csv
import os

FILE_NAME = "expenses.csv"
HEADER = ["date", "amount", "category", "note"]


def init_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)


def add_expense():
    print("\n🧾 Add a New Expense")
    print("-" * 25)

    date = input("📅 Date (YYYY-MM-DD): ").strip()
    amount = input("💰 Amount: ").strip()
    category = input("🏷️  Category: ").strip()
    note = input("📝 Note (optional): ").strip()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])

    print("✅ Expense saved successfully!")


def main():
    init_csv()
    print("=== 💼 Expense Input System ===")

    while True:
        add_expense()
        cont = input("➕ Add another expense? (y/n): ").lower()
        if cont != "y":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
