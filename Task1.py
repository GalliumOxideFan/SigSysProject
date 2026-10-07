import numpy as np
import control as ct
import matplotlib.pyplot as plt

G = 1
R = 1
R2 = 1
R3 = 1
C = 1

num1 = [-1]
den1 = [(R*C/G)**2, R2/R3*R*C/G, 1]

num2 = [-1,0]
den2 = [R*C/G, R2/R3, G/R*C]

num3 = [-1,0,0]
den3 = [1, R2/R3 * G/(R*C), (G/(R*C))**2]

H1 = ct.tf(num1, den1)
H2 = ct.tf(num2, den2)
H3 = ct.tf(num3, den3)

plt.figure()
out = ct.pole_zero_plot(H3)
plt.show()


y1, t1 = ct.matlab.impulse(H1)
y2, t2 = ct.matlab.impulse(H2)
y3, t3 = ct.matlab.impulse(H3)

fig, axs = plt.subplots(1,3)

axs[0,0].plot(t1,y1)
axs[0,0].set_title('H1')

axs[0,1].plot(t2,y2)
axs[0,1].set_title('H2')

axs[0,2].plot(t3,y3)
axs[0,2].set_title('H3')

for ax in axs.flat:
    ax.set_xlabel("t [s]")
    ax.grid(True)

fig.tight_layout()
plt.show()