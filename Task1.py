import numpy as np
import control as ct
import matplotlib.pyplot as plt

G = 1
R = 1
R2 = 1
R3 = 1
C = 1

num = [-1,0,0]
den = [1, R2/R3 * G/(R*C), (G/(R*C))**2]

H3 = ct.tf(num, den)

plt.figure()
out = ct.pzplot(H3)
plt.show()
