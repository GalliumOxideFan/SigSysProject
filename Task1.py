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
out = ct.pzplot(H3)
plt.show()
