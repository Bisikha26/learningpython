import numpy as np
from matplotlib import pyplot as plt

l = float(input("Enter the length of beam: "))
q = float(input("Enter the loading intensity"))

x = np.linspace(0, l, 20)
M = q/2*(l*x-x**2)
V = q*(l/2-x)

plt.figure(figsize=(10, 4))
plt.plot([0]*int(l+1), color='k')
plt.plot(x, -M)
# plt.plot(M)
# plt.plot(V)
plt.fill(x, -M,"c")
plt.show()

