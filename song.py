
import numpy as np
import scipy.io.wavfile
import winsound

from constants import *

def add(s, t):
  if len(s) == 0: return t
  if len(s) != len(t): raise NameError("Added track size must match song size.")
  return s + t

def write(x, name, volume=1.0):
  A = volume * (2**15-1) # int16 scale factor; 2^16/2, since signed, -1 to avoid saturation
  x *= A/np.max(np.abs(x)) # normalize the signal to span the int16 domain
  scipy.io.wavfile.write(name, fs, x.astype(np.int16))

def loop(s, f):
  play(s, f, loop=True)

def play(s, f, loop=False):
  f = "./songs/" + f
  write(s, f, volume=1.0)
  play = True
  while (play):
    winsound.PlaySound(f, 0)
    play = loop