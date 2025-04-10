from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        values = [float(request.form.get(key)) for key in request.form if key != 'datetime']

        # Dummy prediction logic
        co = random.uniform(0.5, 1.5)
        co2 = random.uniform(1.0, 2.5)
        ratio = round(co / co2, 4)

        # Dummy model metrics
        accuracy = round(random.uniform(93, 96), 2)
        mse = round(random.uniform(0.001, 0.01), 4)

        # Generate future values for chart
        future_values = [round(ratio + random.uniform(-0.05, 0.05), 4) for _ in range(4)]

        return render_template("result.html",
                               prediction=ratio,
                               accuracy=accuracy,
                               mse=mse,
                               future_values=future_values)
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
