## Front End Code

# Importing Requirements
import streamlit as st
import BackEndCode as bec

# Page Setup
st.set_page_config(
    page_title = "Home",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

# Initializing Output
output = "Yet to be generated"

# Page Title
st.title("Hybrid Encryptor")

# Adding Blank Lines
for i in range(3):
    st.write("")

# Creating Columns in Page
col1, col2 = st.columns(
    spec = 2,
    gap = "large"
)

# Setting Elements on the Left Column
with col1:
    # Input Box for Plaintext
    message = st.text_input(
        label = "Input",
        key = "Plaintext", 
        placeholder = "Enter Input here"
    )

    # Drop Down Box for Selecting Algorithm
    available_algorithms = ["Mono-alphabetic Cipher", "Vigenere Cipher", "Vernam Cipher", "One-Time Pad", "Hybrid"]
    algorithm = st.selectbox(
        label = "Select the Algorithm",
        options = available_algorithms,
        index = 0,
        key = "Algorithm Choice"
    )

    # Checking if Algorithm is Hybrid
    if algorithm == "Hybrid":
        # Drop Down Box for Hybrid Algorithm
        hybrid_algorithm = st.selectbox(
            label = "Select the Algorithm",
            options = ["Mono-alphabetic with Vigenere", "Vernam with Vigenere", "Vernam with Mono-alphabetic"],
            index = 0,
            key = "Hybrid Algorithm Choice"
        )
    else:
        hybrid_algorithm = 0

    # Radio Selection for Operation
    available_options = ["Encrypt", "Decrypt"]
    option = st.radio(
        label = "Operation",
        options = available_options,
        index = 0,
        key = "Operation Choice"
    )    

    # Input Box for Key
    key = st.text_input(
        label = "Key",
        key = "Key",
        placeholder = "Enter Key here"
    )

    # Key Input for Hybrid Algorithm`
    if algorithm == "Hybrid":
      key2 = st.text_input(
        label = "Second Key",
        key = "Second Key",
        placeholder = "Enter Second Key here"
    )
    else:
      key2 = 0

    # Button to Submit
    if st.button(label = "Submit"):
        output = bec.returnOutput(message, algorithm, hybrid_algorithm, option, key, key2)

# Setting Elements on the Right Column
with col2:
    # Printing Output
    st.text("Output:")
    st.write(output)
    