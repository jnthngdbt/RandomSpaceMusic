import numpy as np

import midi
import note

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def sine(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = midi.freq(k)
    sk = note.sine(T=Tk, fx=fk)
    sk = note.tamper(sk, Tf)
    s = np.concatenate((s, sk))
  return s

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def band(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = midi.freq(k)
    sk = note.band(T=Tk, fx=fk)
    sk = note.tamper(sk, Tf)
    s = np.concatenate((s, sk))
  return s