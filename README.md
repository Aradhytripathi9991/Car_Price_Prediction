
🚗 Car Price Predictor
A Streamlit-based web application that predicts the selling price of a used car using an XGBoost Regressor model. Users enter vehicle details through a simple UI and receive an instant estimated price in lakhs.

📌 Overview
This project uses a pre-trained XGBoost model to estimate the selling price of used cars based on key attributes like ex-showroom price, kilometers driven, fuel type, seller type, transmission, and ownership history. The application is built with Streamlit for a quick and interactive user experience.

✨ Features
Interactive Web UI — Clean Streamlit interface with intuitive input controls (number inputs, select boxes, slider)
XGBoost Model — Powered by a pre-trained XGBoost Regressor for accurate price estimation
Real-time Prediction — Instant results with a single button click
Indian Market Focused — Prices displayed in lakhs, tailored to the Indian used car market
🛠️ Tech Stack
Component	Technology
Language	Python 3.9+
ML Model	XGBoost
Web Framework	Streamlit
Data Handling	Pandas, NumPy
📁 Project Structure
car-price-predictor/
├── car_price_prediction.py # Main Streamlit application
├── xg_model.json # Pre-trained XGBoost model file
├── requirements.txt # Python dependencies
└── README.md

text


## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/car-price-predictor.git
   cd car-price-predictor
Install dependencies:
bash

pip install -r requirements.txt
Ensure xg_model.json is present in the same directory as the script.
Run the App
bash

streamlit run car_price_prediction.py
The app will open in your browser at http://localhost:8501.

📊 Input Features
Input Field
Type
Description
Ex-Showroom Price (lakhs)	Number	Original on-road price of the car (2.5 – 25.0)
Kilometers Driven	Number	Total distance the car has been driven
Fuel Type	Select Box	Petrol, Diesel, or CNG
Seller Type	Select Box	Dealer or Individual
Transmission	Select Box	Manual or Automatic
Owner Type	Select Box	First, Second, Third, or Fourth & Above Owner

📈 Model Details
Algorithm: XGBoost Regressor
Input Features (6): Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner
Output: Estimated selling price in lakhs (₹)
Model File: xg_model.json (XGBoost native format)
🧠 How It Works
The app loads the pre-trained XGBoost model from xg_model.json
User enters car details through the Streamlit interface
Categorical inputs (fuel type, seller type, transmission, owner) are label-encoded into numeric values
The encoded features are passed to the model as a Pandas DataFrame
The model returns the predicted selling price, displayed to the user

📝 Requirements:-

streamlit
pandas
numpy
xgboost
🤝 Contributing
Contributions are welcome! Feel free to open a pull request or raise an issue.

📄 License
This project is licensed under the MIT License.

📧 Contact
Aradhy Tripathi




