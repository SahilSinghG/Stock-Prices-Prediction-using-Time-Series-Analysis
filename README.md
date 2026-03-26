# 📈 Stock Price Prediction using LSTM

## 📌 Project Overview

Stock price prediction is a challenging problem due to the dynamic and volatile nature of financial markets. Investors and analysts rely on historical data patterns to estimate future price movements.

This project builds a Deep Learning model using Long Short-Term Memory (LSTM) networks to predict future stock prices based on historical stock market data.

The model learns temporal patterns from past stock prices and forecasts the next day's closing price. The project demonstrates a complete end-to-end machine learning pipeline, including:

Data collection
Exploratory Data Analysis (EDA)
Data preprocessing
Time series sequence creation
Deep learning model training
Model evaluation
Deployment using Streamlit

## Project Structure

<img width="720" height="416" alt="image" src="https://github.com/user-attachments/assets/7450b82b-6c35-4c12-a858-8856e0b25867" />

## 🎯 Problem Statement

The goal of this project is to predict future stock prices using historical market data.

Stock prices form a time series, where future values depend on past values. Traditional machine learning models struggle with sequential dependencies, which is why Recurrent Neural Networks (RNNs) and specifically LSTM networks are used.

LSTM models are capable of learning long-term dependencies in sequential data, making them well suited for financial time-series forecasting.

## 📊 Dataset

Stock data was obtained using the Yahoo Finance API via the yfinance Python library.

Example stock used in this project:

Apple (AAPL)
Dataset Features
Column	Description
Open	Price when the market opened
High	Highest price during the day
Low	Lowest price during the day
Close	Closing price
Volume	Number of shares traded

For prediction, the Closing Price was used because it is the most commonly analyzed metric in financial forecasting.

## 🔍 Exploratory Data Analysis (EDA)

Before training the model, exploratory data analysis was performed to understand market trends.

Stock Price Trend

The closing price over time was visualized to observe long-term trends.

<img width="1068" height="742" alt="image" src="https://github.com/user-attachments/assets/132c15bc-7de8-4fa5-bd67-0585929c777d" />

Daily Return Analysis

<img width="1033" height="707" alt="image" src="https://github.com/user-attachments/assets/b7fbb0fe-dd58-4c2b-b891-0f337f108104" />

Daily returns were calculated to measure price volatility.

Moving Averages

<img width="952" height="752" alt="image" src="https://github.com/user-attachments/assets/8fbdb135-58b8-4e6b-8235-baae73243dc0" />

Moving averages were used to smooth short-term fluctuations and identify trends:

50-day moving average
200-day moving average
Correlation Analysis

A correlation heatmap was created to analyze relationships between stock features such as Open, High, Low, Close, and Volume.

<img width="951" height="717" alt="image" src="https://github.com/user-attachments/assets/1e1b3668-db31-44b9-b245-c7a9879fa408" />

These analyses help understand market behavior before building predictive models.

## ⚙️ Data Preprocessing

Deep learning models require normalized data.

Scaling

Stock prices were scaled using MinMaxScaler to transform values between 0 and 1.

Scaled value = (x - min) / (max - min)

Scaling improves neural network convergence and training stability.

🔁 Creating Time Sequences

Time series models require sequential inputs.

A sliding window approach was used:

Past 60 days of prices → Predict next day price

Example:

Day1, Day2, Day3 ... Day60 → Predict Day61

This transforms the dataset into sequences suitable for LSTM training.

## 🧠 Model Architecture

A Sequential LSTM Neural Network was used.

Model architecture:

1️⃣ LSTM Layer (50 units)
2️⃣ Dropout Layer (regularization)
3️⃣ LSTM Layer (50 units)
4️⃣ Dropout Layer
5️⃣ Dense Output Layer

Dropout layers help prevent overfitting by randomly disabling neurons during training.

## ⚙️ Model Training

The model was trained using:

Optimizer: Adam
Loss Function: Mean Squared Error (MSE)
Epochs: 10
Batch Size: 32

The Adam optimizer was chosen because it provides efficient gradient updates and faster convergence.

## 📈 Model Evaluation

Model performance was evaluated using Root Mean Squared Error (RMSE).

Example result:

RMSE ≈ 6.13

This means that the predicted stock price differs from the actual price by approximately $6 on average.

Because stock markets are influenced by many external factors (news, economic events, market sentiment), achieving perfect prediction is impossible. However, the model successfully captures the overall trend of stock price movements.

## 📉 Prediction Visualization

Predicted prices were plotted against actual prices.

<img width="948" height="750" alt="image" src="https://github.com/user-attachments/assets/e3ba67d8-8b25-4eb3-92e3-e6be57402cff" />

The visualization shows that the predicted price curve follows the general direction and trend of the real stock prices, indicating that the model successfully learns temporal patterns.

## 💾 Model Saving

The trained LSTM model was saved for later use in deployment.

model.save("lstm_stock_model.h5")

This file is loaded by the Streamlit application to generate predictions.

## 🌐 Deployment

The trained model was deployed using Streamlit, allowing users to interact with the model through a web interface.

Users can enter a stock symbol such as:

AAPL

TSLA

GOOGL

The application then predicts the next day's closing stock price.

<img width="1273" height="385" alt="image" src="https://github.com/user-attachments/assets/710d0ced-ebce-4f92-bb0b-86899c684c3c" />

<img width="1320" height="382" alt="image" src="https://github.com/user-attachments/assets/cace8bc2-0cc3-4d28-85af-9ffdc344d0a2" />

<img width="1222" height="372" alt="image" src="https://github.com/user-attachments/assets/fab87394-cf78-42dd-b56e-600a431cba81" />

## 🚀 How to Run the Project

Clone the repository
git clone https://github.com/SahilSinghG/Stock-Prices-Prediction-using-Time-Series-Analysis.git

Install dependencies
pip install -r requirements.txt

Run the Streamlit application
streamlit run app/app.py

The web interface will open in your browser.

## 🛠️ Technologies Used

Python
Pandas
NumPy
Matplotlib
Scikit-learn
TensorFlow / Keras
Streamlit
Yahoo Finance API (yfinance)

## 📌 Key Skills Demonstrated

This project demonstrates several important data science skills:

Time Series Analysis
Deep Learning using LSTM
Financial Data Analysis
Feature Scaling
Sequence Modeling
Model Evaluation
Machine Learning Deployment

## 📊 Future Improvements

Possible enhancements include:

Predicting multiple stocks simultaneously
Adding technical indicators such as RSI, MACD, and Bollinger Bands
Using advanced architectures like GRU networks
Deploying the model with FastAPI and Docker

## 👨‍💻 Author

Sahil Singh

Machine Learning & Data Science Enthusiast

GitHub:
https://github.com/SahilSinghG
