import argparse
import numpy as np
import pandas as pd

import Models.ARIMA
import Transformations.waveletTransform

key = "7DDXDYF9IGHOIYJX" #alpha-vantage

transforms = {'wavelet': Transformations.waveletTransform.waveletTransformer}
models = {'ARIMA': Models.ARIMA.arima}

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-data', help='company code')
    parser.add_argument('-model', help='model to perform prediction')
    parser.add_argument('-transform', help='transform data')
    parser.add_argument('-showpredict', help='plot predicted trend', action='store_true')
    args = parser.parse_args()

    data_csv_name = "Data/" + args.data + ".csv"
    stock_prices = pd.read_csv(data_csv_name, index_col='timestamp')[::-1]
    stock_prices.index = np.linspace(0, len(stock_prices)-1, len(stock_prices))

    transformed_data = stock_prices
    if (args.transform):
        transformer = transforms[args.transform](stock_prices)
        transformed_data = transformer.transform_plot()

    if (args.model):
        model_object = models[args.model](stock_prices)
        model_object.fit()
        model_object.predict_plot(stock_prices)

if __name__ == "__main__":
    main()