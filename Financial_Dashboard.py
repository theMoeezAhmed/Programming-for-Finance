import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import random

# Define a list of financial tips
financial_tips = [
    "Set aside at least 20% of your income for savings.",
    "Track your expenses daily to identify areas for cuts.",
    "Automate your savings to make it a consistent habit.",
    "Review and renegotiate bills like insurance and subscriptions periodically.",
    "Build an emergency fund that covers 3-6 months of expenses.",
    "Avoid unnecessary debt by planning major purchases in advance.",
    "Invest early to take advantage of compound interest.",
    "Diversify your investments to reduce risk.",
    "Set specific financial goals and track your progress.",
    "Regularly review your budget and adjust as needed."
]

# --------------------------
# Sidebar Navigation
# --------------------------
st.sidebar.title("📊 Financial Dashboard")
page = st.sidebar.radio("Select a Section:", 
                        ["🏠 Overview", "📈 Financial Metrics", "💡 Recommendations", "💡 Daily Tip"])

# --------------------------
# Overview Page
# --------------------------
if page == "🏠 Overview":
    st.title("💰 Enhanced Financial Health Dashboard")
    st.write("""
    Welcome to your all-in-one financial health tool! Here, you can:
    
    - **Analyze key financial metrics** such as net income, savings rate, debt-to-income ratio, and emergency fund coverage.
    - **Visualize your expense distribution** and compare different components of your income.
    - **Receive personalized recommendations** to improve your financial well-being.
    - **Get a daily financial tip** to stay motivated.
    """)
    st.info("Use the sidebar to navigate through different sections.")

# --------------------------
# Financial Metrics Page
# --------------------------
elif page == "📈 Financial Metrics":
    st.title("📊 Your Financial Metrics")
    
    # --- User Inputs ---
    st.subheader("Enter Your Current Financial Details")
    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Monthly Income ($):", min_value=0.0, value=5000.0, step=100.0)
        expenses = st.number_input("Monthly Expenses ($):", min_value=0.0, value=3000.0, step=100.0)
    with col2:
        savings = st.number_input("Monthly Savings ($):", min_value=0.0, value=1000.0, step=50.0)
        debt = st.number_input("Total Debt ($):", min_value=0.0, value=20000.0, step=500.0)
    emergency_fund = st.number_input("Emergency Fund ($):", min_value=0.0, value=5000.0, step=100.0)
    
    # --- Calculations ---
    net_income = income - expenses - savings
    savings_rate = (savings / income) * 100 if income > 0 else 0
    debt_income_ratio = (debt / income) if income > 0 else 0
    emergency_coverage = (emergency_fund / expenses) if expenses > 0 else 0

    # Display metrics with conditional formatting
    st.write("## Key Metrics")
    col1, col2 = st.columns(2)
    
    col1.metric("Net Income", f"${net_income:,.2f}", delta_color="off")
    col1.metric("Savings Rate", f"{savings_rate:.1f}%", delta_color="normal")
    col2.metric("Debt-to-Income Ratio", f"{debt_income_ratio:.2f}", delta_color="inverse")
    col2.metric("Emergency Fund Coverage", f"{emergency_coverage:.1f} months", delta_color="normal")

    # --- Expense Distribution Visualization ---
    remaining_income = max(income - expenses - savings, 0)
    labels = ["Savings", "Expenses", "Remaining Income"]
    values = [savings, expenses, remaining_income]
    
    st.write("### Expense Distribution")
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, 
           colors=["#1f77b4", "#ff7f0e", "#2ca02c"],
           wedgeprops={"edgecolor": "white", "linewidth": 2})
    ax.axis("equal")
    st.pyplot(fig)

# --------------------------
# Recommendations Page
# --------------------------
elif page == "💡 Recommendations":
    st.title("💡 Personalized Recommendations")
    
    st.write("Based on your financial details, here are some suggestions to improve your financial well-being:")
    
    # --- Input for Recommendations ---
    with st.expander("Enter Financial Details for Personalized Insights"):
        income_rec = st.number_input("Monthly Income ($):", min_value=0.0, value=5000.0, step=100.0, key="inc_rec")
        expenses_rec = st.number_input("Monthly Expenses ($):", min_value=0.0, value=3000.0, step=100.0, key="exp_rec")
        savings_rec = st.number_input("Monthly Savings ($):", min_value=0.0, value=1000.0, step=50.0, key="sav_rec")
        debt_rec = st.number_input("Total Debt ($):", min_value=0.0, value=20000.0, step=500.0, key="debt_rec")
        emergency_fund_rec = st.number_input("Emergency Fund ($):", min_value=0.0, value=5000.0, step=100.0, key="em_rec")
    
    if income_rec:
        net_income_rec = income_rec - expenses_rec - savings_rec
        savings_rate_rec = (savings_rec / income_rec) * 100 if income_rec > 0 else 0
        debt_income_ratio_rec = (debt_rec / income_rec) if income_rec > 0 else 0
        emergency_coverage_rec = (emergency_fund_rec / expenses_rec) if expenses_rec > 0 else 0

        st.write("#### Your Key Financial Indicators:")
        st.write(f"- **Net Income:** ${net_income_rec:,.2f}")
        st.write(f"- **Savings Rate:** {savings_rate_rec:.1f}%")
        st.write(f"- **Debt-to-Income Ratio:** {debt_income_ratio_rec:.2f}")
        st.write(f"- **Emergency Fund Coverage:** {emergency_coverage_rec:.1f} months")
        
        st.write("#### Recommendations:")
        if savings_rate_rec < 20:
            st.warning("💡 Try to increase your savings rate to at least 20% for better financial stability.")
        else:
            st.success("✅ Your savings rate is healthy!")
    
        if debt_income_ratio_rec > 1:
            st.warning("⚠️ High debt-to-income ratio detected! Consider debt consolidation or prioritizing high-interest loans.")
        else:
            st.success("✅ Your debt is within a manageable range.")
    
        if emergency_coverage_rec < 3:
            st.warning("🚨 Your emergency fund is low! Aim for at least 3-6 months of coverage.")
        else:
            st.success("✅ Your emergency fund is in a strong position.")
    else:
        st.info("🔹 Enter your details to receive personalized recommendations.")

# --------------------------
# Daily Financial Tip Page
# --------------------------
elif page == "💡 Daily Tip":
    st.title("💡 Daily Financial Tip")
    # For consistency, set seed based on today's date so the tip remains the same for the day
   
    tip_of_the_day = random.choice(financial_tips)
    
    st.write("### Tip of the Day")
   
    st.info(tip_of_the_day)
    st.write("Remember: Small, consistent actions can lead to significant financial improvements over time!")
