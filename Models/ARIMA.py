from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt


class arima():
    '''
    Simple Arima model with default order (5,1,5)
    '''
    data = None #entire data set
    relevant_column = ['open'] #single column
    model = None
    DEFAULT_ORDER = (5, 1, 5)
    DEFAULT_TRAIN_PERCENTAGE = 0.9 # first PERCENTAGE of data used for fitting
    DEFAULT_TEST_PERCENTAGE = 0.05 #forecasting out of sample time step equals 5% of original data length

    def __init__(self, data):
        self.data = data

    def fit(self):
        self.model = ARIMA(endog=self.data[self.relevant_column], order=self.DEFAULT_ORDER).fit(trend='c')

    def predict_plot(self, is_dynamic=False):

        prediction_start = int(round(self.DEFAULT_TRAIN_PERCENTAGE * len(self.data.index),0))
        prediction_end = int(round(len(self.data.index) * (1 + self.DEFAULT_TEST_PERCENTAGE),0))

        predicted_trend = self.model.predict(start=prediction_start, end=prediction_end, dynamic=False, typ='levels')
        plt.plot(predicted_trend)
        plt.plot(self.data[self.relevant_column].loc[prediction_start:])
        plt.show()

    def change_parameter(self, new_parameter_triple):
        assert(len(new_parameter_triple)==3) # check if new paramter is size 3
        self.DEFAULT_ORDER = new_parameter_triple

    def replace_data(self, new_data):
        self.data = new_data
