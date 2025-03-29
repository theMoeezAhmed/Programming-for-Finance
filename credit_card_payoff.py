# -*- coding: utf-8 -*-
"""credit_card_payoff.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zxfp6gwOsdkoo149HJjsDbqc8hh7wrhJ
"""

pip install streamlit ngrok
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_minimum_payment(balance, apr, min_payment_pct):
    monthly_rate = apr / 12 / 100
    months = 0
    total_interest = 0
    data = []
    while balance > 0:
        interest = balance * monthly_rate
        payment = max(balance * min_payment_pct / 100, interest + 10)  # Ensuring at least interest + $10 is paid
        balance -= (payment - interest)
        total_interest += interest
        months += 1
        data.append((months, balance, total_interest))
        if months > 300:  # Avoid infinite loops
            break
    return data, total_interest

def calculate_fixed_payment(balance, apr, fixed_payment):
    monthly_rate = apr / 12 / 100
    months = 0
    total_interest = 0
    data = []
    while balance > 0:
        interest = balance * monthly_rate
        payment = min(balance + interest, fixed_payment)  # If payment is larger than balance + interest, pay off in full
        balance -= (payment - interest)
        total_interest += interest
        months += 1
        data.append((months, balance, total_interest))
        if months > 300:  # Avoid infinite loops
            break
    return data, total_interest

def plot_results(min_data, fix_data, min_total_int, fix_total_int):
    min_months, min_balances, _ = zip(*min_data)
    fix_months, fix_balances, _ = zip(*fix_data)

    fig, ax = plt.subplots()
    ax.plot(min_months, min_balances, label=f"Minimum Payment (Interest: ${min_total_int:.2f})", linestyle='dashed')
    ax.plot(fix_months, fix_balances, label=f"Fixed Payment (Interest: ${fix_total_int:.2f})", linestyle='solid')

    ax.set_xlabel("Months")
    ax.set_ylabel("Remaining Balance ($)")
    ax.set_title("Credit Card Payoff Comparison")
    ax.legend()
    st.pyplot(fig)

def main():
    st.title("💳 Credit Card Payoff Planner")

    st.sidebar.header("Input Your Details")
    balance = st.sidebar.number_input("Credit Card Balance ($)", min_value=100.0, value=5000.0, step=100.0)
    apr = st.sidebar.number_input("Annual Interest Rate (APR%)", min_value=1.0, max_value=50.0, value=20.0, step=0.1)
    min_payment_pct = st.sidebar.number_input("Minimum Payment Percentage (%)", min_value=1.0, max_value=10.0, value=3.0, step=0.1)
    fixed_payment = st.sidebar.number_input("Fixed Monthly Payment ($)", min_value=10.0, value=200.0, step=10.0)

    if st.sidebar.button("Calculate Plan"):
        min_data, min_total_int = calculate_minimum_payment(balance, apr, min_payment_pct)
        fix_data, fix_total_int = calculate_fixed_payment(balance, apr, fixed_payment)

        st.subheader("Payoff Comparison")
        plot_results(min_data, fix_data, min_total_int, fix_total_int)

        st.write(f"💡 **Total Interest Paid with Minimum Payment:** ${min_total_int:.2f}")
        st.write(f"💡 **Total Interest Paid with Fixed Payment:** ${fix_total_int:.2f}")

        if fix_total_int < min_total_int:
            st.success("✅ Fixed payments save you money on interest!")
        else:
            st.warning("⚠️ Minimum payments take longer and cost more in interest!")


if __name__ == "__main__":
    main()

!streamlit run credit_card_payoff.py
