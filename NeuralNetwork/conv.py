import numpy as np


class convLayer:

    def __init__(self, dim: int, num_filters: int):
        self.dim = dim
        self.num_filters = num_filters
        self.padding = 0
        self.filters = None   # lazy init
        self.bias = None

    def CreateRegions(self, input):
        h, w, _ = input.shape

        for i in range(h - self.dim + 1):
            for j in range(w - self.dim + 1):
                region = input[i:(i + self.dim), j:(j + self.dim), :]
                yield region, i, j

    def ForwardPass(self, input):

        # Ensure input is 3D (H,W,C)
        if input.ndim == 2:
            input = input[:, :, None]

        h, w, c = input.shape

        # Lazy filter initialization
        if self.filters is None:
            rng = np.random.default_rng()
            fan_in = self.dim * self.dim * c
            scale = np.sqrt(2 / fan_in) # Scale factor for He initialization

            self.filters = rng.standard_normal(
                size=(self.num_filters, self.dim, self.dim, c)
            ) * scale
            self.bias = np.zeros(self.num_filters)

        output = np.zeros((h - self.dim + 1, w - self.dim + 1, self.num_filters))

        for region, i, j in self.CreateRegions(input):
            # sum over (dim, dim, channels)
            output[i, j] = np.sum(region * self.filters, axis=(1, 2, 3)) + self.bias

        return output
    
    def BackProp(self, ):
        pass