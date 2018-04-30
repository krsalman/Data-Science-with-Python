import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2

plt.plot(x,y,'r')
plt.xlabel('x Label')
plt.ylabel('y Label')
plt.title('Title')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(x,y,'b')
plt.show()

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x,'g')

plt.show()

fig , axes = plt.subplots(1,2)

axes[0].plot(x,y)

axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')

plt.show()

fig , axes = plt.subplots(2,1,figsize=(7,3))

axes[0].plot(x,y,'r')
axes[0].set_title('First Plot')

axes[1].plot(y,x,'b')
axes[1].set_title('second Plot')

plt.tight_layout()

plt.show()


