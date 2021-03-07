import numpy as np
import scipy.signal

from constants import *

def time(T):
  return np.arange(0,T,dt)

def sine(T=2, fx=1000):
  t = time(T)
  x = np.sin(2*np.pi*fx*t + np.random.rand()) # add random phase
  return x

# fl: low pass frequency
def noise(T=2, fl=1000):
  t = time(T)
  N = len(t)

  order = 2
  sos = scipy.signal.butter(order, (fl/nyquist), 'lowpass', output='sos')

  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)

  return x

def band(T=2, fx=1000, df=None):
  t = time(T)
  N = len(t)

  if df is None:
    df = fx/50

  lf = (fx-df)/nyquist
  hf = (fx+df)/nyquist
  order = 20
  sos = scipy.signal.butter(order, [lf, hf], 'bandpass', output='sos')

  # The signal is bandpass filtered white noise.
  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)

  return x

def frequency(k):
  d = 8 # 4
  return 2 ** (k/octave) * (440 / d)

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def generateSineSeq(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = frequency(k)
    sk = sine(T=Tk, fx=fk)
    sk = tamper(sk, Tf)
    s = np.concatenate((s, sk))
  return s

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def generateNoiseToneSeq(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = frequency(k)
    sk = band(T=Tk, fx=fk)
    sk = tamper(sk, Tf)
    s = np.concatenate((s, sk))
  return s

# x: signal to tamper
# Tt: sum of tamper period left and right
def tamper(x, Tt, type='hann'):
  Nt = int(Tt*fs)
  w = scipy.signal.windows.get_window(type, Nt)

  Nlhs = int(np.floor(0.5*Nt))
  Nrhs = Nt - Nlhs

  x[:Nlhs] *= w[:Nlhs]
  x[-Nrhs:] *= w[-Nrhs:]

  return x

def reverb(x, delay=4000, decay=0.8):
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