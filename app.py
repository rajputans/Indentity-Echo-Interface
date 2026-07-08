import streamlit as st

# ------------------------------
# The Identity Echo Interface
# ------------------------------

st.set_page_config(
    page_title="The Identity Echo Interface",
    page_icon="📡",
    layout="centered"
)

# Task 1
st.title("📡 The Identity Echo Interface")
st.write("Enter your name and message below, then click Transmit.")

# Task 2
user_name = st.text_input("Enter your Name")
user_message = st.text_input("Enter your Message")

# Task 3
if st.button("Transmit"):

    # Task 4
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    else:

        # Task 5
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # ------------------------------
        # Advanced Challenge
        # ------------------------------

        character_count = len(user_message)

        token_count = round(character_count / 4, 2)

        st.info(
            f"System Check: Your message will consume approximately {token_count} tokens from our context window."
        )