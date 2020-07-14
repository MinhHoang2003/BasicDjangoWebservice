import os.path

import pandas as pd
from sklearn.linear_model import LinearRegression


def predict(temp, humid):
    project_path = os.path.abspath(os.path.dirname(__name__))
    data = pd.read_csv(project_path + '/predict_api/ai/hn_weather_data.csv', encoding='utf-8')

    X = data[['Temperature', 'Humidity']]

    y = data["Precipitation"]
    y = y.values.reshape(-1, 1)

    regr = LinearRegression()
    regr.fit(X, y)
    return regr.predict([[temp, humid]]).__float__()
