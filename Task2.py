import numpy as np
import control as ct
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fft

Tmax = 0.06
fs = 24000

def f(t):
    return np.sin(4000*2*np.pi*t) + 0.5*np.sin(17000*2*np.pi*t)

num, den = signal.butter(12,2*np.pi*8000, btype='low', analog=True)

H = ct.tf(num,den)

def sampling(func, fs, Tmax):
    T = np.linspace(0, Tmax, 1000*int(fs*Tmax))
    t_out, u = ct.forced_response(H, T, func(T))

    u = np.round(2**11*u[::1000])/2**11
    return t_out[::1000], u

t = np.linspace(0,Tmax,100000)
uin = f(t)
t1, y1 = ct.forced_response(H, t, uin)
T, y = sampling(f, fs, Tmax)
# plt.scatter(T, y)
# plt.plot(t1, y1)
# plt.show()

fft_result = np.fft.rfft(y)
freq = np.fft.rfftfreq(len(T), 1/fs)
plt.plot(freq/1000,np.abs(fft_result)/(fs*Tmax/2))
plt.xlabel('Frequency [kHz]')
plt.ylabel('Amplitude')
# ct.bode_plot(H)
plt.show()
