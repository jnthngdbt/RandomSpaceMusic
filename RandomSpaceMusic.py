import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal

matplotlib.style.use('dark_background')

fs = 44100 # Hz, WAV file sampling frequency
dt = 1/fs # sec

def getTimeDomain(T):
  return np.arange(0,T,dt)

def plotSound(x):
  T = dt*len(x)
  t = getTimeDomain(T)

  plt.figure()
  plt.plot(t, x, '.-', markersize=3, linewidth=1)
  plt.xlabel('time (s)')
  plt.ylabel('sound')

  f = np.fft.fftfreq(len(x), dt)
  F = np.fft.fft(x)

  plt.figure()
  plt.plot(f, np.real(F), '.-', markersize=3, linewidth=1)
  plt.xlabel('frequency (Hz)')
  plt.ylabel('amplitude')
  plt.title('FFT')

def writeWav(x, name, volume=0.9):
  A = volume * 2**15 # int16 scale factor; 2^16/2, since signed
  x *= A/np.max(x) # normalize the signal to span the int16 domain
  scipy.io.wavfile.write(name, fs, x.astype(np.int16))

def generateSine(T=2, fx=1000):
  t = getTimeDomain(T)
  x = np.sin(2*np.pi*fx*t)
  return x

def generateNoiseMode(T=2, fx=1000):
  t = getTimeDomain(T)
  N = len(t)

  nyq = fs/2
  df = fx/30
  lf = (fx-df)/nyq
  hf = (fx+df)/nyq
  order = 10
  sos = scipy.signal.butter(order, [lf, hf], 'bandpass', output='sos')

  # The signal is bandpass filtered white noise.
  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)

  return x

# s = generateSine(T=4, fx=5000)

def getNoteFrequency(k):
  return 2 ** (k/12) * 440

k0 = 0
f0 = getNoteFrequency(k0)
f1 = getNoteFrequency(k0+4)
f2 = getNoteFrequency(k0+5)
f3 = getNoteFrequency(k0+7)

s1 = generateNoiseMode(T=4, fx=f0) + generateNoiseMode(T=4, fx=f1)
s2 = generateNoiseMode(T=4, fx=f0) + generateNoiseMode(T=4, fx=f2)
s3 = generateNoiseMode(T=4, fx=f0) + generateNoiseMode(T=4, fx=f3)
s = np.concatenate((s1,s2,s3))

writeWav(s, "noisemode.wav")

# plotSound(s)

plt.show()
