import numpy as np


class convLayer:

    def __init__(self, dim: int, num_filters: int):
        # Initialize properties of the class
        self.dim = dim
        self.num_filters = num_filters
        self.padding = int(np.ceil((self.dim - 1) / 2))


        # Initialize the conv_layer filters as arrays of dimention (dim, dim, conv_layer)
        rng = np.random.default_rng() # We create a rng generator to initialize the values of our filters
        self.filters = rng.standard_normal(size = (self.num_filters, self.dim, self.dim)) # We use the rng gen to fill the array with base values

    def CreateRegions(self, input):
        # Get dimentions of the image
        h, w = input.shape

        # Create the nxn regions to do the convolution
        for i in range(h - 2*self.padding):
            for j in range(w - 2*self.padding):

                region = input[i : (i + self.dim), j : (j + self.dim)] # We extract the region to convolve 
            yield region, i, j # Return the region and its top left coordinate in the total array
        
    def ForwardPass(self, input):
        # Do the convolution and apply an activation function
        h, w = input.shape

        # Initialize the output array with the correct sizes
        output = np.zeros((h - 2*self.padding, w - 2*self.padding, self.num_filters)) 

        # Iterate over the needed regions and apply the convolution
        for region, i, j in self.CreateRegions(input):
            output[i, j] = np.sum(region * self.filters, axis = (1,2))
        return output