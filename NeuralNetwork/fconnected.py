import numpy as np

class FullyConnected:

    def __init__(self, outputs: int):
        self.outputs = outputs
        self.weights = None
        self.bias = None

    def ForwardPass(self, input):

        # Flatten everything except batch
        x = input.flatten()

        if self.weights is None:
            rng = np.random.default_rng()
            self.weights = rng.standard_normal(
                size=(self.outputs, x.size)
            )
            self.bias = np.zeros(self.outputs)

        output = self.weights @ x + self.bias
        return output
    
    def BackProp(self, ):
        pass