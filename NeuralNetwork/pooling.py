import numpy as np


# Create the maxpool class which takes the max value of a region of size (size x size) and outputs a single value
class Maxpool:

    def __init__(self, size: int = 2, stride: int = 2):

        # Define size of the maxpool filter size should be a power of 2 and stride the same
        self.size = size
        self.stride = stride

        self.filter = np.zeros((self.size, self.size))

    def CreateRegions(self, input):
        # Get dimentions of the input array
        h, w, d = input.shape

        # Create n x n regions for pooling spacin them by the stride size
        for i in range(int(h / self.stride)):
            for j in range(int(w / self.stride)):
                region  = input[self.stride * i: self.stride * i + self.size, self.stride * j: self.stride * j + self.size]

                yield region, i, j # Return the region and its coordinate

    def pool(self, input):
        # Get dimentions of the input array
        h, w, d = input.shape

        # Initialize output array with the size (h / stride, w / stride )
        output = np.zeros((int(h / self.stride), int(w / self.stride)))

        # Iterate over the needed regions and apply the convolution
        for region, i, j in self.CreateRegions(input):
            output[i, j] = np.max(region)
        return output