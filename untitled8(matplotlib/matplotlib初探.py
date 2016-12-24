import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)
plt.figure(figsize=(8,4))
plt.plot(x,y,label='$sin(x)$')
plt.plot(x,z,"b--",label='$cos(x)$')
plt.xlabel("Time(s)")
plt.ylabel("")
plt.title("matplotlib")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()