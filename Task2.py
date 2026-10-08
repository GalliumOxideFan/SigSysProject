import numpy as np
import control as ct
import matplotlib.pyplot as plt
from scipy import signal

num, den = signal.butter(25,2*np.pi*8000, btype='low', analog=True)

H = ct.tf(num,den)

ct.bode_plot(H)
plt.show()
