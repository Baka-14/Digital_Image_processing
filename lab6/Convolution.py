# Plotting a 1D convoluted graph
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,1000,80)
x1 = np.cos(x)**2
x2 = np.tanh(x)*(np.sin(x)**2)

print(x.shape, x1.shape, x2.shape)

conv_1d = np.convolve(x1, x2)

print(conv_1d.shape)

plt.figure(figsize=(30,15))

plt.subplot(211)
plt.title("2 signals", fontsize = 10) 
plt.plot(x, x1)
plt.plot(x, x2)
plt.subplot(212)
plt.title("1D Convoluted signal", fontsize =10)
plt.plot(conv_1d)
plt.show()