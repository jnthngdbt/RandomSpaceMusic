import numpy as np
import scipy.signal

import midi

from constants import *

def time(T):
  return np.arange(0,T,dt)

def length(T):
  return fs*T

def silent(T=2):
  return np.zeros(length(T))

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
