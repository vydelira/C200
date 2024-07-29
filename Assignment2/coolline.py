import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
x = np.arange(0, 10.0, 0.2)

# red dashes
plt.plot(x, x**2 + 2*x + 2, 'g--' )
plt.plot(x, x**3, 'r^')
plt.plot(x, x*4 - 3, 'b')
plt.xlabel("My Inputs")
plt.ylabel("My Outputs")
plt.title("My Graph")
plt.show()
