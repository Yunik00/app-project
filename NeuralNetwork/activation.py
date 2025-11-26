import numpy as np


class Leakyrelu:

    def __init__(self, damping=0.01):
        self.damping = damping

    def ForwardPass(self, input):
        return np.maximum(self.damping * input, input)
    
    def BackProp(self, ):
        pass

class Softmax:

    def __init__(self):
        pass

    def ForwardPass(self, input):

        # subtract max for numerical stability
        shifted = input - np.max(input)

        exp_vals = np.exp(shifted)

        return exp_vals / np.sum(exp_vals)
    
    def BackProp(self, ):
        pass