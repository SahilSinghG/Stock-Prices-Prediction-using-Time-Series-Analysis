import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

model = keras.models.load_model("models/lstm_stock_model.h5")

st.title("📈 Stock Price Prediction")

ticker = st.text_input("Enter Stock Symbol (Example: AAPL)", "AAPL")

df = yf.download(ticker, start="2015-01-01", end="2024-01-01")

data = df[['Close']]

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)

last_60_days = scaled_data[-60:]
last_60_days = np.reshape(last_60_days,(1,60,1))

prediction = model.predict(last_60_days)
prediction = scaler.inverse_transform(prediction)

st.write("Predicted Next Day Price:")
st.success(f"${prediction[0][0]:.2f}")