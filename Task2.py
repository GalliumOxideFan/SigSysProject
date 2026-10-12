import numpy as np
import control as ct
import matplotlib.pyplot as plt
from scipy import signal

Tmax = 0.06 # End of signal [s]
fs = 24000 # Sampling frequency [Hz]
OSR = 1000 # Oversampling rate for "analog" simulation

f_1 = 4000 # The frequencies of the input signal [Hz]
f_2 = 17000 

def f(t): # Function for the input signal
    return np.sin(4000*2*np.pi*t) + 0.5*np.sin(17000*2*np.pi*t) # Input signal consisting of two siniodals

butt = signal.butter(12,8000, btype='low', fs = fs*OSR, output="sos") # Get the transfer function for a butterworth filter with order 12 and cut off frequency 8 Khz
# We use output="sos" to make it output as second-order sections, which basically means putting a bunch of second order filters in series instead of one high order filter
# We do this because otherwise the coefficients of the filter would be huge and prone to errors that makes the filter unstable due to computational rounding errors


def sampling(func, fs, Tmax): # Emulate sampling the input signal (func) between t=0 and (Tmax) at sampling frequency (fs) through an anti-aliasing filter
    T = np.linspace(0, Tmax, OSR*int(fs*Tmax))  # We cannot use an analog filter in a computer so we approximate an anolog filter by using a sampling rate 1000 times larger than the actual rate
    u = signal.sosfilt(butt, func(T)) # Apply the analog butterworth anti-aliasing filter to the "analog" signal
    u = np.round(2**11*u[::OSR])/2**11 # Get the samples by taking every thousand output from the "analog" output, then apply quantisation in accordance to the 12 bit bus
    
    return T[::OSR], u # Return the output signal and its time steps

t = np.linspace(0,Tmax,100000) # t for plotting an approximation of the non digitalised output
#uin = f(t)
#t1, y1 = ct.forced_response(H, t, uin) # "Analog" output
T, y = sampling(f, fs, Tmax) # Digitalised output
# plt.scatter(T, y)
# plt.plot(t1, y1)
# plt.show()

fft_result = np.fft.rfft(y) # Gets the amplitudes
freq = np.fft.rfftfreq(len(T), 1/fs) # Gets the positive frequencies

# Plots the fourier transform of the digital output
plt.plot(freq/1000,np.abs(fft_result)/(fs*Tmax/2)) # Plots with frequency in kHz and amplitude normalised
plt.xlabel('Frequency [kHz]')
plt.ylabel('Amplitude')
plt.show()
