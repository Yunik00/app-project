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
Test = np.random.rand(64, 64 )*255


# Create Layers
conv = convolution.convLayer(3,8)
activ = act.Leakyrelu(0.5)
maxpool = pooling.Maxpool(2,2)
conv2 = convolution.convLayer(3,8)
activ2 = act.Leakyrelu(1)
maxpool2 = pooling.Maxpool(2,2)
con = conect.FullyConnected(10)
activ3 = act.Softmax()

def Forward(image, label):
    
    # Do a forward pass and calculate acuracy and cross-entropy loss

    # Transform the image from [0,255] to [-0.5 , 0.5]
    out = image / 255 - 0.5

    # Do the forward operations    
    out = conv.ForwardPass(out)
    print("Primera convolucion")
    print("activacion")
    out = activ.ForwardPass(out)
    print("pooling")
    out = maxpool.ForwardPass(out)
    out = conv2.ForwardPass(out)
    print("resultado de la convolucion")
    out = activ2.ForwardPass(out)
    print("activacion")
    print("pooling")
    out = maxpool2.ForwardPass(out)
    out = con.ForwardPass(out)
    out = activ3.ForwardPass(out)

    # Calculate Cross-entropy loss and acuracy

    loss = -np.log(out[label])
    acc = 1 if np.argmax(out) == label else 0

    return out, loss, acc


def generate_9(size=64, thickness=5):
    img = np.zeros((size, size))

    cx, cy = size // 2, size // 2
    r = size // 4

    # Draw the circular top of the 9
    for i in range(size):
        for j in range(size):
            dist = np.sqrt((i - cy)**2 + (j - cx)**2)
            if r - thickness < dist < r + thickness and i < cy:
                img[i, j] = 255

    # Draw the vertical tail of the 9
    for i in range(cy, size - 10):
        for j in range(cx + r//2 - thickness, cx + r//2 + thickness):
            img[i, j] = 255

    return img

# ✅ Generate the test digit
nine = generate_9()

print(nine.shape)   # (64, 64)

# ✅ Visualize it
plt.imshow(nine, cmap="gray")
plt.title("Synthetic Digit 9 (64x64)")
plt.axis("off")
plt.show()

loss = 0
num_correct = 0 
out, l, acc = Forward(nine, 9)

print(out.shape)
print(out)
print(np.sum(out))
print(l)
print(acc)