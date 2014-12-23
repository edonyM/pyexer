import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 5.0, 0.01)
plt.figure(1)
plt.subplot(121)
plt.plot(t1, f(t1), 'bo' , t2, f(t2), 'k')
plt.title("Histogram",fontsize=14, color='blue')
plt.xlabel("Smart")
plt.ylabel("Probablility")
plt.text(3, 0.5, r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.axis([0, 5, -1, 1])
plt.subplot(122)
plt.plot(t2, np.cos(2*np. pi*t2), 'r')
#plt.show()
#plt.figure(2)
#plt.plot(t1, np.sin(2*np.pi*t1, 'g')
#plt.figure(1)
plt.figure(2)
plt.plot(t3, np.sin(2*np.pi*t3), 'g')
plt.show()
