import pandas as pd


class Zero_one_loss:
    def compute(self, estimate , parameter):
        assert isinstance(estimate, pd.Series) and isinstance(parameter, pd.Series)
        loss = estimate.tolist() != parameter.tolist()
        return 0 if loss ['True'] == None else loss ['True']