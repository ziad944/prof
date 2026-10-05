
import pandas as pd
import streamlit as st

from tracker import ExpenseTracker
from charts import category_chart, monthly_chart, daily_chart


tracker = ExpenseTracker()
tracker.load()


st.title("Expense Tracker")


# Add Expense
amount = st.number_input(
    "Amount",
    min_value=0.0
)

category = st.selectbox(
    "Category",
    ["Food", "Transport", "Shopping", "Bills", "Other"]
)

date = st.date_input("Date")

note = st.text_input("Note")


if st.button("Add Expense"):
    tracker.add_expense(
        amount,
        category,
        date,
        note
    )

    tracker.save()

    st.success("Expense added successfully!")


# Statistics
total, average, maximum = tracker.total_expenses()

st.subheader("Statistics")

st.metric("Total Expenses", total)
st.metric("Average Expense", average)
st.metric("Highest Expense", maximum)


# Expenses by Category
category_expenses = tracker.expenses_by_category()

st.subheader("Expenses by Category")

st.dataframe(category_expenses)

fig = category_chart(category_expenses)

st.pyplot(fig)


# Expenses by Month
monthly_expenses = tracker.expenses_by_month()

st.subheader("Expenses by Month")

st.dataframe(monthly_expenses)

fig = monthly_chart(monthly_expenses)

st.pyplot(fig)


# Expenses by Day
daily_expenses = tracker.expenses_by_day()

st.subheader("Expenses by Day")

st.dataframe(daily_expenses)

fig = daily_chart(daily_expenses)

st.pyplot(fig)


# All Expenses
st.subheader("All Expenses")

df = pd.DataFrame(
    tracker.expenses,
    columns=["amount", "category", "date", "note"]
)

st.dataframe(df)

