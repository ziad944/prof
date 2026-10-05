
import pandas as pd
import numpy as np


class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: int, category: str, date, note: str):
        add = [
            float(amount),
            category,
            date,
            note
        ]

        self.expenses.append(add)

    def save(self):
        df = pd.DataFrame(
            self.expenses,
            columns=["amount", "category", "date", "note"]
        )

        df.to_csv("expenses.csv", index=False)

    def load(self):
        try:
            df = pd.read_csv("expenses.csv")

            df["amount"] = pd.to_numeric(
                df["amount"],
                errors="coerce"
            )

            df = df.dropna(subset=["amount"])

            self.expenses = df.values.tolist()

        except FileNotFoundError:
            self.expenses = []

    def total_expenses(self):
        amounts = []

        for expense in self.expenses:
            amounts.append(float(expense[0]))

        if not amounts:
            return 0, 0, 0

        total = np.sum(np.array(amounts, dtype=float))
        average = np.mean(np.array(amounts, dtype=float))
        maximum = np.max(np.array(amounts, dtype=float))

        return total, average, maximum

    def expenses_by_category(self):
        df = pd.DataFrame(
            self.expenses,
            columns=["amount", "category", "date", "note"]
        )

        df["amount"] = pd.to_numeric(
            df["amount"],
            errors="coerce"
        )

        result = df.groupby("category")["amount"].sum()

        return result

    def expenses_by_month(self):
        df = pd.DataFrame(
            self.expenses,
            columns=["amount", "category", "date", "note"]
        )

        df["amount"] = pd.to_numeric(
            df["amount"],
            errors="coerce"
        )

        df["date"] = pd.to_datetime(
            df["date"],
            format="mixed"
        )

        df["month"] = df["date"].dt.to_period("M")

        result = df.groupby("month")["amount"].sum()

        return result

    def expenses_by_day(self):
        df = pd.DataFrame(
            self.expenses,
            columns=["amount", "category", "date", "note"]
        )

        df["amount"] = pd.to_numeric(
            df["amount"],
            errors="coerce"
        )

        df["date"] = pd.to_datetime(
            df["date"],
            format="mixed"
        )

        result = df.groupby("date")["amount"].sum()

        return result

