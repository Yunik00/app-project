import numpy as np

class fullyconnected:

    def __init__(self, outputs: int):
        
        self.outputs = outputs
        self.weights = None

    def ForwardPass(self, input):
        h, w = input.shape

        if self.weights is None:
            rng = np.random.default_rng() # We create a rng generator to initialize the values of our filters
            self.weights = rng.standard_normal(size = (self.outputs, h))

        Output = self.weights @ input
        return Output
