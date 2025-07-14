# House-Price-Prediction-Using-Machine-Learning
---
# 🏠 House Price Prediction

This project is a **machine learning web application** that predicts residential house prices based on various property features. It uses an ensemble of regression models to deliver accurate price estimates and provides an intuitive user interface built with Streamlit.

## 📌 Project Overview

The goal of this project is to help buyers, sellers, and real estate agents make informed decisions by providing reliable property price predictions.

Key features:
- Predict house prices using multiple features like area, number of bedrooms/bathrooms, floor, furnishing score, balcony, sector, society cleanliness, and property name.
- Built with an ensemble model combining **Random Forest**, **Gradient Boosting**, and **XGBoost** regressors.
- Hyperparameter tuning with **GridSearchCV** for optimal performance.
- Deployed with **Streamlit**, featuring an interactive form and Lottie animations for a modern UI.
- Clean, modular, and extensible codebase.

## ⚙️ Tech Stack

- **Languages & Libraries:** Python, pandas, scikit-learn, XGBoost, joblib
- **Framework:** Streamlit for frontend & deployment
- **Visuals:** Lottie animations for better UX

## 🚀 How It Works

1. **Data Preparation:**  
   - Data is cleaned and preprocessed with feature engineering, categorical encoding, and scaling.
2. **Model Training:**  
   - Multiple regressors are trained and combined in an ensemble for improved accuracy.
   -  The final model achieves **99.5% accuracy** on the test dataset.
3. **Deployment:**  
   - The final model is saved using `joblib` and integrated into a Streamlit app.
4. **User Interaction:**  
   - Users enter property details through a form and get instant price predictions.

## 🗂️ Project Structure

```

├── app.py             # Streamlit app script
├── data/              # Raw and processed data
├── models/            # Trained models (.pkl or .joblib)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation

```

## 📈 Future Improvements

- Integrate live property listings.
- Add geospatial analysis for location-based price insights.
- Deploy as a full-stack app with a backend database.
- Recommendation system for users

## ✨ Author

**Arshdeep Singh**  
Passionate about data science, machine learning, and building real-world solutions.

---

Feel free to contribute, fork, or share your feedback!

```
