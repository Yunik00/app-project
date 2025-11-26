import numpy as np


# Create the maxpool class which takes the max value of a region of size (size x size) and outputs a single value
class Maxpool:

    def __init__(self, size: int = 2, stride: int = 2):
        self.size = size
        self.stride = stride

    def CreateRegions(self, input):
        h, w, _ = input.shape

        for i in range(0, h - self.size + 1, self.stride):
            for j in range(0, w - self.size + 1, self.stride):

                region = input[i:i+self.size, j:j+self.size, :]
                yield region, i // self.stride, j // self.stride

    def ForwardPass(self, input):
        h, w, c = input.shape

        out_h = (h - self.size) // self.stride + 1
        out_w = (w - self.size) // self.stride + 1

        output = np.zeros((out_h, out_w, c))

        for region, i, j in self.CreateRegions(input):
            output[i, j] = np.max(region, axis=(0, 1))

        return output
    
    def BackProp(self, ):
        pass
    
    # Create the avgpool class which takes the max value of a region of size (size x size) and outputs a single value
class Avgpool:

    def __init__(self, size: int = 2, stride: int = 2):
        self.size = size
        self.stride = stride

    def CreateRegions(self, input):
        h, w, _ = input.shape

        for i in range(0, h - self.size + 1, self.stride):
            for j in range(0, w - self.size + 1, self.stride):

                region = input[i:i+self.size, j:j+self.size, :]
                yield region, i // self.stride, j // self.stride

    def ForwardPass(self, input):
        h, w, c = input.shape

        out_h = (h - self.size) // self.stride + 1
        out_w = (w - self.size) // self.stride + 1

        output = np.zeros((out_h, out_w, c))

        for region, i, j in self.CreateRegions(input):
            output[i, j] = np.mean(region, axis=(0, 1))

        return output
    
    def BackProp(self, ):
        pass