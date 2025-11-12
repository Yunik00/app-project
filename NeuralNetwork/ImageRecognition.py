import numpy as np
import matplotlib.pyplot as plt
import activation as activation
import conv as convolution
import activation as act
import pooling as pooling
import fconnected as conect

# Variables
# definir tamaño del input
# definir numero y tamaño de las hidden layers
# definir funcion de salida
# cantidad de salidas


##. Testeo random
Test = np.random.rand(256, 256 )*255


conv = convolution.convLayer(4,3)
activ = act.Leakyrelu(0.5)
maxpool = pooling.Maxpool(2,2)
conv2 = convolution.convLayer(4,3)
activ2 = act.Leakyrelu(1)
avgpool = pooling.Avgpool(2,2)
con = conect.fullyconnected(10)
activ3 = act.Softmax()

print(Test.shape)
a = conv.ForwardPass(Test)
print("Primera convolucion")
print("activacion")
b = activ.ForwardPass(a)
print("pooling")
c = maxpool.ForwardPass(b)
d = conv2.ForwardPass(c)
print("resultado de la convolucion")
e = activ2.ForwardPass(d)
print("activacion")
print("pooling")
f = avgpool.ForwardPass(e)
g = f.flatten()
g = g.reshape((-1, 1))
print(g.shape)
h = con.ForwardPass(g)
output = activ3.Forwardpass(h)
print(output.shape)
print(output)
print(np.sum(output))