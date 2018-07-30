import pytest
import pandas as pd
import numpy as np

import MachineLearning.src.LossFunctions as lf


def test_zero_one_loss():
    loss = lf.Zero_one_loss()
    y_est = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
    x_par = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
    assert 0 == loss.compute(y_est, x_par)




test_zero_one_loss()