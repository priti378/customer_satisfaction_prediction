# customer_satisfaction_prediction
live demo-(https://customersatisfactionprediction1.streamlit.app/)

🧠 Project Overview
This application uses a pre-trained machine learning model to predict binary customer satisfaction (Satisfied or Not Satisfied) based on:

Customer Age

Customer Gender

Product Purchased

Issue Type

Ticket Channel

The goal is to assist customer service teams in understanding satisfaction trends based on common ticket attributes.

🚀 Live App
Try it live 👉 https://customersatisfactionprediction1.streamlit.app

🛠 Tools & Technologies
Python

Pandas, NumPy

Scikit-learn

Streamlit

Pickle (model serialization)

💡 Features
Simple and intuitive UI

Takes customer service-related inputs

Binary classification: Satisfied or Not Satisfied

Real-time prediction using a saved ML model

📁 Project Structure
bash
Copy
Edit
├── customer.py                  # Streamlit app
├── satisfaction_model.pkl       # Trained ML model (binary classifier)
├── feature_columns.pkl          # Feature list used for encoding input
├── README.md                    # Project documentation
💻 How to Run Locally
Clone the repo or copy the files into a directory.

Install dependencies:

pip install streamlit pandas scikit-learn numpy
Ensure the following files are in the same directory:

customer.py

satisfaction_model.pkl

feature_columns.pkl

Run the app:
streamlit run customer.py

📦 Sample Input Features
Gender: Male / Female / Other

Age: Integer (18–70)

Product: Amazon Echo, Fire TV, Kindle, etc.

Issue: Billing, Technical, Account, Other

Channel: Email, Chat, Phone

📌 Note
This app uses pre-processed one-hot encoded features. It reindexes the input to match training-time columns using feature_columns.pkl.

The model and its training logic are assumed to have been developed and saved earlier.

👤 Author
Priti Priti
Deployed with ❤️ on Streamlit




