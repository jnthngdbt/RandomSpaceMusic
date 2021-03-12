import numpy as np

import midi
import note

from constants import *

def major(T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[], type=None):
  return signal(scales["major"], T, root, notes, Tf, amps, type)

def minor(T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[], type=None):
  return signal(scales["minor"], T, root, notes, Tf, amps, type)
  
def signal(scale, T=2, root=0, notes=[1,3,5,8], Tf=0, amps=[], type=None):
  if len(amps) == 0: amps = np.ones(len(notes))
  elif len(amps) != len(notes): raise NameError("Number of amps must match number of notes.")

  s = note.silent(T)
  for i, n in enumerate(notes):
    k = midi.number(root, n, scale)
    f = midi.freq(k)
    if type == None or type == 'sine':
      s += amps[i] * note.sine(T=T, fx=f, Tf=Tf)
    elif type == 'peak':
      s += amps[i] * note.peak(T=T, fx=f, Tf=Tf)

  s = note.normalize(s)
  return s