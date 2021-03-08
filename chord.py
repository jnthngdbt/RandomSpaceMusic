import midi
import note

from constants import *

def major(T=2, root=0, notes=[1,3,5,8], Tf=0):
  return signal(scales["major"], T, root, notes, Tf)

def minor(T=2, root=0, notes=[1,3,5,8], Tf=0):
  return signal(scales["minor"], T, root, notes, Tf)
  
def signal(scale, T=2, root=0, notes=[1,3,5,8], Tf=0):
  s = note.silent(T)
  for n in notes:
    k = midi.number(root, n, scale)
    f = midi.freq(k)
    s += note.sine(T, f, Tf)
  return s