import numpy as np
import control as ct
import matplotlib.pyplot as plt

G = 1 # Scales all axis, no shange in shape
R = 1 # Scales all axis, no shange in shape, opposite sacling to G
R2R3 = 1 # R2/R3 Low large imaginary part of the poles compared to real values, a lot of oscillation in the impulse response. Also an amplification seen in the bode, where we have resonace. Opposite for high values. 
C = 1 # Scales all axis, no shange in shape, opposite sacling to G

num1 = [-1]
den1 = [(R*C/G)**2, R2R3*R*C/G, 1]

num2 = [-1,0]
den2 = [R*C/G, R2R3, G/R*C]

num3 = [-1,0,0]
den3 = [1, R2R3 * G/(R*C), (G/(R*C))**2]

H1 = ct.tf(num1, den1)
H2 = ct.tf(num2, den2)
H3 = ct.tf(num3, den3)

# Poles plotting
fig, axs = plt.subplots(1,3, figsize = (10,4))

ct.pole_zero_plot(H1, ax=axs[0])
ct.pole_zero_plot(H2, ax=axs[1])
ct.pole_zero_plot(H3, ax=axs[2])

axs[0].set_title('H1')

axs[1].set_title('H2')

axs[2].set_title('H3')

for ax in axs.flat:
    ax.grid(True)

fig.tight_layout()
plt.show()


# Impulse response plot
t1, y1 = ct.impulse_response(H1)
t2, y2 = ct.impulse_response(H2)
t3, y3 = ct.impulse_response(H3)

fig, axs = plt.subplots(1,3,figsize = (10,4))

axs[0].plot(t1,y1)
axs[0].set_title('H1')

axs[1].plot(t2,y2)
axs[1].set_title('H2')

axs[2].plot(t3,y3)
axs[2].set_title('H3')

for ax in axs.flat:
    ax.set_xlabel("t [s]")
    ax.grid(True)

fig.tight_layout()
plt.show()


# Bode plots

ct.bode_plot(H1)
plt.show()

ct.bode_plot(H2)
plt.show()

ct.bode_plot(H3)
plt.show()
