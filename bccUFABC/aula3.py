import numpy as np
import matplotlib.pyplot as plt
'''
x1 = np.arange(-25,25.1,0.1)
y1 = np.cos(x1)
x2 = np.arange(-15, 15.1, 0.1)
y2 =  np.sqrt(222 - x2**2)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
'''
x = np.arange(-10,10,1)
y1 = x*x
y2 = -x*x
y3 = x

plt.plot(x,y1,'b.-', label = 'trajetória 1')
plt.plot(x,y2,'ro', label = 'reflexo')
plt.plot(x,y3,'g', label = 'reta')



plt.title("Meu gráfico")
plt.grid()
plt.xlabel("tempo")
plt.ylabel("pontos")

plt.legend()



plt.show()
