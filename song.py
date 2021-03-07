
import numpy as np
import scipy.io.wavfile
import winsound

from constants import *

def write(x, name, volume=0.9):
  A = volume * 2**15 # int16 scale factor; 2^16/2, since signed
  x *= A/np.max(x) # normalize the signal to span the int16 domain
  scipy.io.wavfile.write(name, fs, x.astype(np.int16))

def play(s, f, loop=False):
  f = "./songs/" + f
  write(s, f, volume=1.0)
  play = True
  while (play):
    winsound.PlaySound(f, 0)
    play = loop