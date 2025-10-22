import numpy as np
import matplotlib.pyplot as plt
import activation as activation
import conv as conv
import pooling as pooling


# Variables
# definir tamaño del input
# definir numero y tamaño de las hidden layers
# definir funcion de salida
# cantidad de salidas

Test = np.ones((6,6))
Test2 = np.array([[1,2,3,4],
         [2,4,1,2],
         [1,1,1,6],
         [0,3,5,1]])

conv = conv.convLayer(2,3)
maxpool = pooling.Maxpool(2,2)

print(Test)
print(conv)
print(maxpool)

print("convolution")
pass1 = conv.ForwardPass(Test)
print(pass1)

print("pooling")
result = maxpool.pool(pass1)

print(result)