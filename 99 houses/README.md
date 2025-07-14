# 📁 Models Directory

This folder contains the trained machine learning models for the **House Price Prediction** project.

## 📌 Contents

- **Trained Models:**  
  Includes the final trained ensemble model and any individual base models (Random Forest, Gradient Boosting, XGBoost) saved in `.joblib` or `.pkl` format.
  
- **Versioning:**  
  Models are versioned with clear filenames to keep track of updates and improvements.

Example files:
```

├── random\_forest\_model.joblib

````

## ⚙️ Usage

These models are loaded in the **Streamlit app (`app.py`)** for making predictions.  

To update or retrain:
1. Retrain your models in your notebook or training script.
2. Save updated models to this directory:
   ```python
   import joblib
   joblib.dump(model, 'models/flat_price_prediction.pkl')
````

3. Restart your Streamlit app to use the new version.

## 🔒 Note

* Keep your models organized to avoid confusion.
* Store only the latest, tested models here.
* Do not commit sensitive training data or intermediate files.

## ✨ Author

**Arshdeep Singh**
House Price Prediction Project — Model Directory.

```

---

This `README` clearly explains **what’s inside your `/models` folder**, **how to use it**, and **basic version control tips**.  

If you’d like, I can also create one for your **`data/` folder** — just say *yes*!
```
