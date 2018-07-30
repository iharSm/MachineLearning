from MachineLearning.src.Context import Context

class NNT:

    def __init__(self):
        print ("Initializing NNT...\n")
        self.context = Context()

    def compute_loss(self,  estimate , parameter):
        return self.context["loss_function"].compute(estimate, parameter)