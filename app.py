ind=0
b=1781373
count = 0
a=8000
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
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
    # sales.plot()
    # plt.show()
    # from statsmodels.graphics.tsaplots import plot_acf
    # plot_acf(sales)
    # plt.show()
    # sales_diff = sales.diff(periods=1)
    # sales_diff = sales_diff[1:]
    # print(sales_diff.head())
    # plot_acf(sales_diff)
    # plt.show()
    # sales_diff.plot()
    # plt.show()

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

    #
    #
    # from statsmodels.tsa.arima_model import ARIMA
    #
    # #p,d,q  p = periods taken for autoregressive model
    # #d -> Integrated order, difference
    # # q periods in moving average model
    # #print(train)
    # # Build Model
    # # model = ARIMA(train, order=(3,2,1))
    # model = ARIMA(train, order=(1,1, 1))
    # fitted = model.fit(disp=-1)
    #
    # # Forecast
    # fc, se, conf = fitted.forecast(15, alpha=0.05)  # 95% conf
    # #print('hello',test)
    # # Make as pandas seriesg
    # fc_series = pd.Series(fc)
    # lower_series = pd.Series(conf[:, 0])
    # upper_series = pd.Series(conf[:, 1])
    #
    # # Plot
    # plt.figure(figsize=(12,5), dpi=100)
    # plt.plot(train, label='training')
    # plt.plot(test, label='actual')
    # plt.plot(fc_series, label='forecast')
    # plt.fill_between(lower_series.index, lower_series, upper_series,
    #                  color='k', alpha=.15)
    # plt.title('Forecast vs Actuals')
    # plt.legend(loc='upper left', fontsize=8)
    # plt.show()
    # plt.plot(predictions,color='red')
    #
    # print(mean_squared_error(test,predictions))
    #
    # import itertools
    # p=d=q=range(0,5)
    # pdq = list(itertools.product(p,d,q))
    # #print(pdq)
    # import warnings
    # warnings.filterwarnings('ignore')
    # for param in pdq:
    #     try:
    #         model_arima = ARIMA(train,order=param)
    #         model_arima_fit = model_arima.fit()
    #         #print(param,model_arima_fit.aic)
    #     except:
    #         continue


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    global a
    global b
    global count
    import random
    # Data Format
    # [TIME, India, World]
    India=dg()
    India = random.randint(a,a+10)
    a=a+1000
    print(India)
    World = random.randint(b,b+random.randint(0,20000))
    b+=20000
    data = [time() * 1000,abs(India), World]

    response = make_response(json.dumps(data))
    if(count==20):
        exit()
    count+=1

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
