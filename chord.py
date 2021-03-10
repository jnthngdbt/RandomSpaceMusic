import numpy as np

import midi
import note

from constants import *

def major(T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[]):
  return signal(scales["major"], T, root, notes, Tf, amps)

def minor(T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[]):
  return signal(scales["minor"], T, root, notes, Tf, amps)
  
def signal(scale, T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[]):
  if len(amps) == 0: amps = np.ones(len(notes))
  elif len(amps) != len(notes): raise NameError("Number of amps must match number of notes.")

  s = note.silent(T)
  for i, n in enumerate(notes):
    k = midi.number(root, n, scale)
    f = midi.freq(k)
    s += amps[i] * note.sine(T, f, Tf)

  s = note.normalize(s)
  return s