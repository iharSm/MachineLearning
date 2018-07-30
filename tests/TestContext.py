import pytest
import pandas as pd
import numpy as np
from MachineLearning.src.NNT import NNT


def test_LossFunctionContext():
    nnt = NNT()
    y_est = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
    x_par = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
    assert 0 == nnt.compute_loss(y_est, x_par)



test_LossFunctionContext()