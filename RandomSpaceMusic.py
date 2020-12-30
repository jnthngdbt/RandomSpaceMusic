import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
import winsound

matplotlib.style.use('dark_background')

fs = 44100 # Hz, WAV file sampling frequency
dt = 1/fs # sec
nyquist = fs/2 # Hz
octave = 12

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

  df = fx/50
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
  return 2 ** (k/octave) * (440 / d)

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
def tamperSignal(x, Tt, type='hann'):
  Nt = int(Tt*fs)
  # w = scipy.signal.windows.hann(Nt) # similar to hamming but starts/ends at 0
  w = scipy.signal.windows.get_window(type, Nt) # similar to triang but starts/ends at 0

  Nlhs = int(np.floor(0.5*Nt))
  Nrhs = Nt - Nlhs

  x[:Nlhs] *= w[:Nlhs]
  x[-Nrhs:] *= w[-Nrhs:]

  return x

def addSimpleReverb(x, delay=4000, decay=0.8):
  for i in np.arange(delay, len(x)):
    x[i-delay] = decay * x[i]
  return x

#        || .|  | .|  | .|  | .|  | .|  |  | .|  |  | .|                                                                                           
# G-----22-23 24 25 26 27-28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# D-----17-18 19 20 21 22-23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# A-----12-13 14 15 16 17-18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# E-----07-08 09 10 11 12-13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# B-----02-03 04 05 06 07-08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#
# 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G#
# 0                                   1                                   2                                   3                                  
#
# G-----------------------------------------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------
# D--------------------------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15---------------------------------------------
# A-----------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------------------------------------
# E--------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15---------------------------------------------------------------------------
# B-----0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------------------------------------------------------------------

# A  = 12, As = 13, B = 14, C = 15, Cs = 16, D = 17, Ds = 18, E = 19, F = 20, Fs = 21, G = 22, Gs = 23
def A (i): return  0 + octave * i
def As(i): return  1 + octave * i
def B (i): return  2 + octave * i
def C (i): return  3 + octave * i
def Cs(i): return  4 + octave * i
def D (i): return  5 + octave * i
def Ds(i): return  6 + octave * i
def E (i): return  7 + octave * i
def F (i): return  8 + octave * i
def Fs(i): return  9 + octave * i
def G (i): return 10 + octave * i
def Gs(i): return 11 + octave * i

def Ab(i): return Gs(i-1)
def Bb(i): return As(i)
def Cb(i): return B(i)
def Db(i): return Cs(i)
def Eb(i): return Ds(i)
def Fb(i): return E(i)
def Gb(i): return Fs(i)

def Bs(i): return C(i)
def Es(i): return F(i)

def sharp(notes): return np.array(notes) + 1
def flat(notes): return np.array(notes) - 1