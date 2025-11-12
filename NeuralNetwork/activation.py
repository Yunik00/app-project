import numpy as np


class Leakyrelu:
    
    def __init__(self,damping):
        
        self.damping = damping
    
    def ForwardPass(self, input):
        
        h, w, d= input.shape
        output = np.zeros((h,w,d))

        for i in range(h):
            for j in range(w):
                for l in range(d):
                    output[i, j, l] = np.max((self.damping * input[i, j, l], input[i, j, l]))


        return output

class Softmax:
    
    def __init__(self):
        pass

    def Forwardpass(self, input):
        
        output = np.exp(input)

        return output / np.sum(output)
        
        
