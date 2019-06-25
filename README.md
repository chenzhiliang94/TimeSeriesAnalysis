# TimeSeriesAnalysis
Framework for testing, validating and brainstorming

# Dependencies:
- Numpy
- Pandas
- Statsmodels
- matplotlib
- pywt

# General way of running the code
- `python main.py` + `-d *STOCK_NAME*` + `-m *MODEL_NAME*`

# To transform time series data
- On command line, run `python main.py -d GOOG -m ARIMA`
- GOOG is the name of the csv data in `Data` directory; ARIMA is the name of the Model class in `Model` directory.

# To perform prediction
- On command line, run `python main.py -d GOOG -t wavelet`
- wavelet is the name of the transformation class in `Transformations` directory.

# To add a new model
- Create a new model class in `Models` as a Python file

# To add a new transformation
- Create a new Transformation class in `Transformations` as a Python file

# To add a new time series data
- Add the csv file into the `Data` directory
