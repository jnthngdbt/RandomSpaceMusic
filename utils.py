import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from constants import *

matplotlib.style.use('dark_background')

def plot(x):
  if (len(x) <= 0):
    return
    
  T = dt*len(x)
  t = np.arange(0,T,dt)

  plt.figure()

  plt.subplot(1,2,1)
  plt.plot(t, x, '.-', markersize=3, linewidth=1)
  plt.xlabel('time (s)')
  plt.ylabel('sound')

  f = np.fft.fftfreq(len(x), dt)
  F = np.fft.fft(x)

  plt.subplot(1,2,2)
  plt.plot(f, np.abs(F), '.-', markersize=3, linewidth=1)
  plt.xlabel('frequency (Hz)')
  plt.ylabel('amplitude')
  plt.title('FFT')

  plt.show()