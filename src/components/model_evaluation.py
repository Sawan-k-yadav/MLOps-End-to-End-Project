import os
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from dataclasses import dataclass
from src.logger.logging import logging
from src.exception.exception import customException

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customException(e, sys)

