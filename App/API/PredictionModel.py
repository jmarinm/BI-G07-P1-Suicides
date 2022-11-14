from joblib import dump,load
import numpy as np
from sklearn.metrics import mean_squared_error as mse

class Model:

    def __init__(self):
        self.model = load("assets/pipeline.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
