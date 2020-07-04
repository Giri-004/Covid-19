
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
print(__name__)
app = Flask(__name__ )
def dg():
    global ind
    import pandas as pd
    from pandas import datetime
    import matplotlib.pyplot as plt
    from statsmodels.tsa.stattools import adfuller
    sales = pd.read_csv("C://Users/Giri/PycharmProject/pro/data/covid.csv")

    sales['Date'] = pd.to_datetime(sales.Date)
    ds=sales['Date']
    sales.set_index("Date", inplace=True)
    train = sales.values[0:75]  # 27 data as train data
    test = sales.values[75:]  # 9 data as test data

    predictions = []

    from statsmodels.tsa.ar_model import AR
    from sklearn.metrics import mean_squared_error
    model_ar = AR(train)
    model_ar_fit = model_ar.fit()

    predictions = model_ar_fit.predict(start=75, end=100)

    # print(predictions)
    # print(test)

    # plt.plot(test)
    # plt.plot(predictions, color='red')
    # plt.show()
    print(predictions, test)
    print(predictions.size, test.size)
    redata=[ds[75:],predictions]

    if(ind+1<len(predictions)):
        ind+=1
        return predictions[ind]
    ind=0
    return predictions[ind]



@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

count = 0
@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, India, World]
    global count
    x = dg()
    India=x[0]


    print(India)
    World = x[1]
    data = [time() * 1000,abs(India[count]), World[count]]

    response = make_response(json.dumps(data))
    if(count==20):
        exit()
    count+=1

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
