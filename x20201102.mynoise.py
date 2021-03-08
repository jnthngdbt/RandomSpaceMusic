import numpy as np

from constants import *

import midi
import note
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
  h1 = 1.0 * generateMyNoiseTrack(notes=midi.flat([ midi.B(1), midi.G(0),  midi.D(1), midi.A(1)])) # flat([B(1), G(0), D(1), A(1)]) # sharp([A(1), F(0), C(1), G(0)])
  h2 = 0.7 * generateMyNoiseTrack(notes=midi.flat([midi.Gb(1), midi.B(1), midi.Gb(1), midi.E(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  h3 = 0.3 * generateMyNoiseTrack(notes=midi.flat([ midi.D(1), midi.D(1),  midi.A(1), midi.Db(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  s = r1 + h1 + h2 + h3
  return s, "song.mynoise.net.1.major.wav"

# ----------------------

s, f = songMyNoiseNet1Major()
song.loop(s, f)
