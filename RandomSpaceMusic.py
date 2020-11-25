import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal

matplotlib.style.use('dark_background')

fs = 44100 # Hz, WAV file sampling frequency
dt = 1/fs # sec
nyquist = fs/2 # Hz

def getTimeDomain(T):
  return np.arange(0,T,dt)

def writeWav(x, name, volume=0.9):
  A = volume * 2**15 # int16 scale factor; 2^16/2, since signed
  x *= A/np.max(x) # normalize the signal to span the int16 domain
  scipy.io.wavfile.write(name, fs, x.astype(np.int16))

def generateSine(T=2, fx=1000):
  t = getTimeDomain(T)
  x = np.sin(2*np.pi*fx*t + np.random.rand()) # add random phase
  return x

def generateNoiseTone(T=2, fx=1000):
  t = getTimeDomain(T)
  N = len(t)

  df = fx/100
  lf = (fx-df)/nyquist
  hf = (fx+df)/nyquist
  order = 20
  sos = scipy.signal.butter(order, [lf, hf], 'bandpass', output='sos')

  # The signal is bandpass filtered white noise.
  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)

  return x

def generateNoise(T=2, fx=1000):
  t = getTimeDomain(T)
  N = len(t)

  order = 2
  sos = scipy.signal.butter(order, (fx/nyquist), 'lowpass', output='sos')

  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)

  return x

def getNoteFrequency(k):
  d = 8 # 4
  return 2 ** (k/12) * (440 / d)

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def generateNoiseToneSeq(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = getNoteFrequency(k)
    sk = generateNoiseTone(T=Tk, fx=fk)
    sk = tamperSignal(sk, Tf)
    s = np.concatenate((s, sk))
  return s

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def generateSineSeq(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = getNoteFrequency(k)
    sk = generateSine(T=Tk, fx=fk)
    sk = tamperSignal(sk, Tf)
    s = np.concatenate((s, sk))
  return s

# x: signal to tamper
# Tt: sum of tamper period left and right
def tamperSignal(x, Tt):
  Nt = int(Tt*fs)
  # w = scipy.signal.windows.hann(Nt) # similar to hamming but starts/ends at 0
  w = scipy.signal.windows.bartlett(Nt) # similar to triang but starts/ends at 0

  Nlhs = int(np.floor(0.5*Nt))
  Nrhs = Nt - Nlhs

  x[:Nlhs] *= w[:Nlhs]
  x[-Nrhs:] *= w[-Nrhs:]

  return x