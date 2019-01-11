import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile

matplotlib.style.use('dark_background')

fs = 44100 # Hz
dt = 1/fs
T = 4 # s
t = np.arange(0,T,dt)
N = len(t)
A = 0.8 * 2**16 # will be int16

fx = 5000 # Hz
x = A * np.sin(2*np.pi*fx*t)

scipy.io.wavfile.write("sine.wav", fs, x.astype(np.int16))

plt.plot(t,x,'.-',markersize=3,linewidth=1)
plt.xlabel('time (s)')
plt.ylabel('sound')
snip = 0.01
plt.xlim([0, snip])
plt.title('Showing {}s/{}s of {}Hz signal ({}Hz)'.format(snip, T, fx, fs))

plt.show()
