import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="🏦 Bank Management System", layout="centered")
st.title("🏦 Simple Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Action",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

st.divider()

if menu == "Create Account":
    st.header("🆕 Create a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if not (name and email and pin):
            st.warning("Please fill all fields.")
        else:
            success, msg = bank.create_account(name, age, email, int(pin))
            if success:
                st.success("✅ Account Created Successfully!")
                st.json(msg)
            else:
                st.error(msg)

elif menu == "Deposit Money":
    st.header("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = bank.deposit_money(acc, int(pin), amount)
        st.success(msg) if success else st.error(msg)

elif menu == "Withdraw Money":
    st.header("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = bank.withdraw_money(acc, int(pin), amount)
        st.success(msg) if success else st.error(msg)

elif menu == "Show Details":
    st.header("📋 View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user, msg = bank.show_details(acc, int(pin))
        if user:
            st.success(msg)
            st.json(user)
        else:
            st.error(msg)

elif menu == "Update Details":
    st.header("✏️ Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New 4-digit PIN (optional)", type="password")

    if st.button("Update"):
        success, msg = bank.update_details(acc, int(pin), name, email, new_pin)
        st.success(msg) if success else st.error(msg)

elif menu == "Delete Account":
    st.header("🗑️ Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
