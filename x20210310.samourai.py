# x20210310.samourai.py

import numpy as np

import midi
import note
import chord
import track
import song

def tone(notes: np.array, k = 0.2):
  N = 5
  notesOut = []
  for n in notes:
    for i in np.arange(N):
      notesOut.append(n + i * 7)

  notesOut.sort()
  amps = np.exp(-k * np.array(notesOut))
  return notesOut, amps

def songSamUrai():
  Tk = 6 # s, for each note
  Tf = Tk
  f0 = 1
  type = 'peak'
  k = 0.23 # harmonics amplitude damp factor (higher: less highs)

  notes, amps = tone([1, 3, 5], k)

  C = chord.major(T=Tk, Tf=Tf, type=type, root=midi.C(f0 + 1), notes=notes, amps=amps)
  G = chord.major(T=Tk, Tf=Tf, type=type, root=midi.G(f0 + 0), notes=notes, amps=amps)
  A = chord.minor(T=Tk, Tf=Tf, type=type, root=midi.A(f0 + 1), notes=notes, amps=amps)
  F = chord.major(T=Tk, Tf=Tf, type=type, root=midi.F(f0 + 0), notes=notes, amps=amps)

  s = []
  t = []

  t = track.riff(t, [C, G, A, F])
  t = track.riff(t, [C, G, A, F])
  t = track.riff(t, [A, G, C, F])
  t = track.riff(t, [A, G, C])

  t = track.append(t, note.silent(T=Tf)) # let the reverb die

  s = track.add(s, t)

  s = note.reverb(s, delay=80000, decay=0.4)

  return s, "song.sam.urai.wav"

s, f = songSamUrai()
song.play(s, f, volume=0.4)