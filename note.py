import numpy as np
import scipy.signal

import midi

from constants import *

def time(T):
  return np.arange(0,T,dt)

def length(T):
  return fs*T

def duration(x):
  return len(x)/fs

def silent(T=2):
  return np.zeros(int(length(T)))

# Tf: fade in/out total
def sine(T=2, fx=1000, Tf=0):
  t = time(T)
  x = np.sin(2*np.pi*fx*t + np.random.rand()) # add random phase
  x = tamper(x, Tf)
  return x

# fl: low pass frequency
def noise(T=2, fl=1000, Tf=0):
  t = time(T)
  N = len(t)

  order = 2
  sos = scipy.signal.butter(order, (fl/nyquist), 'lowpass', output='sos')

  r = np.random.rand(N)
  x = scipy.signal.sosfilt(sos, r)
  x = tamper(x, Tf)
  return x

def band(T=2, fx=1000, df=None, Tf=0):
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
  x = tamper(x, Tf)
  return x

def peak(T=2, fx=1000, q=5, Tf=0):
  t = time(T)
  N = len(t)

  df = fs/N
  bw = fx/q
  Nw = 2 * int(0.5 * bw/df) # enforce even
  w = scipy.signal.windows.get_window('hann', Nw)
  phases = np.exp(1j*np.random.uniform(0, 2*np.pi, (Nw,)))

  X = np.zeros((N,), dtype=complex)
  fi = fx/df
  i1 = max(int(fi-0.5*Nw), 0)
  i2 = min(int(fi+0.5*Nw), N-1)
  X[i1:i2] = w * phases
  x = np.fft.ifft(X).real

  x = tamper(x, Tf)
  return x

# x: signal to tamper
# Tt: sum of tamper period left and right
def tamper(x, Tt, type='hann'):
  if Tt > 0:
    Nt = int(Tt*fs)
    w = scipy.signal.windows.get_window(type, Nt)

    Nlhs = int(np.floor(0.5*Nt))
    Nrhs = Nt - Nlhs

    x[:Nlhs] *= w[:Nlhs]
    x[-Nrhs:] *= w[-Nrhs:]

  return x

def normalize(x):
  m = np.max(np.abs(x))
  if m > 0.0:
    x = np.array(x) / m
  return x

def reverb(x, delay=4000, decay=0.8):
  for i in np.arange(delay, len(x)):
    x[i-delay] = decay * x[i]
  return x
