import numpy as np

import midi
import note

def append(track, s):
  return np.concatenate((track, s))

def riff(chords=[]):
  t = []
  for c in chords:
    t = append(t, c)
  return t

# notes: array of note indexes
# Tk: duration of each note (s)
# Tf: duration of fading in and out (s)
def sine(notes, Tk, Tf):
  s = []
  for k in notes:
    fk = midi.freq(k)
    sk = note.sine(T=Tk, fx=fk)
    sk = note.tamper(sk, Tf)
    s = append(s, sk)
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
    s = append(s, sk)
  return s