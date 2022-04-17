import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(-10,10,1000)
x2=np.linspace(-10,10,1000)
y1=np.exp(x1 - (x1*x1)/2)-1
y2=np.exp(x2 - (x2*x2)/2)*(-1)-1
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()