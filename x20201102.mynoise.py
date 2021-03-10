import numpy as np

from constants import *

import midi
import note
import chord
import track
import song

def generateMyNoiseTrack(notes):
  Tk = 8 # s, for each note
  Tf = Tk # s, time fading in and out

  notes = np.array(notes)
  s = 2 * track.sine(notes=notes, Tk=Tk, Tf=Tf)
  s += 1 * track.sine(notes=notes+octave, Tk=Tk, Tf=Tf) # harmonics

  return s

def songMyNoiseNet1Major():
  r1 = 30.0 * note.band(T=32, fx=midi.freq(midi.Cs(2)))
  h1 = 1.0 * generateMyNoiseTrack(notes=midi.flat([ midi.B(1), midi.G(0),  midi.D(1), midi.A(1)]))
  h2 = 0.7 * generateMyNoiseTrack(notes=midi.flat([midi.Gb(1), midi.B(1), midi.Gb(1), midi.E(1)]))
  h3 = 0.3 * generateMyNoiseTrack(notes=midi.flat([ midi.D(1), midi.D(1),  midi.A(1), midi.Db(1)]))
  s = r1 + h1 + h2 + h3
  return s, "song.mynoise.net.1.major.wav"

def songMyNoiseAFCG():
  Tk = 8 # s, for each note
  Tf = Tk

  s = []
  t = []

  t = track.append(t, chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 3, 5, 8, 10], amps=[3, 1, 2, 1, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Fs(0), notes=[5, 8, 10, 12], amps=[2, 3, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Cs(1), notes=[1, 3, 5, 8, 10], amps=[3, 3, 3, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[3, 5, 8, 10], amps=[3, 3, 2, 1]))

  s = track.add(s, t)
  t = []

  t = track.add(t, 300. * note.peak(T=note.duration(s), Tf=2, fx=midi.freq(midi.Cs(4)), q=5))
  t = track.add(t, 600. * note.peak(T=note.duration(s), Tf=2, fx=midi.freq(midi.Cs(3)), q=8))

  s = track.add(s, t)
  t = []

  return s, "song.mynoise.net.afcg.wav"

# ----------------------

s, f = songMyNoiseAFCG()
# s, f = songMyNoiseNet1Major()
song.loop(s, f)
