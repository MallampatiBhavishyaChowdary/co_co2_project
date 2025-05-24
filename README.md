# 🔥 CO–CO₂ Ratio Prediction App

A sleek Flask web app that predicts the **CO to CO₂ ratio** using randomly simulated values. Visualizes the prediction along with accuracy, MSE, and future trend projections 📈.


## 🚀 How It Works

✨ Fill in the form with industry parameters  
🧠 The app runs a dummy prediction logic (randomized)  
📊 See the predicted CO–CO₂ ratio + accuracy & MSE  
🔮 Watch future ratio values visualized in a chart  



## 🛠️ Tech Stack

- 🐍 Python + Flask
- 🎨 HTML + CSS (Jinja2 Templates)
- 📈 Matplotlib for charting
- 🌐 Bootstrap for styling (optional)


## ⚙️ Getting Started
🔮 Set Up Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


📦 Install Dependencies
bash
Copy
Edit
pip install flask matplotlib numpy


🧙‍♂️ Run the Magic
bash
Copy
Edit
python app.py
App will be available at:
📍 http://localhost:10000

📁 Project Structure
bash
Copy
Edit
co-co2-ratio-predictor/
├── app.py               # Flask app
├── templates/
│   ├── index.html       # Input form UI
│   └── result.html      # Prediction output
├── static/              # CSS or images (optional)
├── requirements.txt     # Dependencies list
└── README.md            # You’re reading this!


📈 Output Preview
✅ CO–CO₂ Ratio: ~1.03

🎯 Accuracy: ~95.12%

❌ MSE: ~0.0041


🔮 Future trend chart included!


📋 Requirements

flask

matplotlib

numpy

Add them to requirements.txt if you're deploying.

💡 About
Built by Mallampati Bhavishya 💙
📍 Final Year CSE Student @ VIT-AP

### 🧬 Clone the Repo

```bash
git clone https://github.com/MallampatiBhavishyaChowdary/co-co2-ratio-predictor.git
cd co-co2-ratio-predictor
