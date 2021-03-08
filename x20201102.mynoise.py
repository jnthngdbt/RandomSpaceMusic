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
  Tf = 8
  T = 4 * Tk

  amps = [1., .7, .3]
  A = chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 5, 3], amps=amps)
  F = chord.major(T=Tk, Tf=Tf, root=midi.Fs(0), notes=[1, 3, 5], amps=amps)
  C = chord.major(T=Tk, Tf=Tf, root=midi.Cs(0), notes=[8, 10, 5], amps=amps)
  G = chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[1, 5, 3], amps=amps)

  drone = 20.0 * note.band(T=T, fx=midi.freq(midi.Cs(2)))

  s = []
  s = song.add(s, track.riff([A, F, C, G]))
  s = song.add(s, drone)

  return s, "song.mynoise.net.afcg.wav"

# ----------------------

s, f = songMyNoiseAFCG()
# s, f = songMyNoiseNet1Major()
song.loop(s, f)
