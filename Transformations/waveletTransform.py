import matplotlib.pyplot as plt
import pywt

class waveletTransformer():
    '''
    wavelet transform for stock prices
    The default decomposition level is 3
    '''
    data=None
    relevant_column = 'open' #single column
    decomposed_data=None
    level = None

    def __init__(self, stock_prices):
        self.data = stock_prices[self.relevant_column]
        print (self.data)

    def transform_plot(self, level=3):
        self.level = level
        self.decomposed_data = pywt.wavedec(self.data, 'db1', mode='cpd' ,level=level)
        self.plot()
        return self.decomposed_data

    def plot(self):
        plt.figure(figsize=(5,10))

        plt.subplot(len(self.decomposed_data)+1, 1, 1)
        plt.title("original data and its wavelet decompositions")
        plt.plot(self.data, c="orange")

        for index, de_level in enumerate(self.decomposed_data):
            plt.subplot(len(self.decomposed_data)+1, 1, index + 2)
            plt.plot(de_level)
        #plt.suptitle(str(self.level) + ' levels of decomposition')
        plt.show()

    def change_parameter(self, new_level):
        assert(isinstance(new_level, int)) #check if new_level is integer
        self.level = new_level

    def replace_data(self, new_data):
        self.data = new_data





