import note
from song import *

def generateMyNoiseSeq(notes):
  Tk = 8 # s, for each note
  Tf = Tk # s, time fading in and out

  notes = np.array(notes)
  s = 2 * note.generateSineSeq(notes=notes, Tk=Tk, Tf=Tf)
  s += 1 * note.generateSineSeq(notes=notes+octave, Tk=Tk, Tf=Tf) # harmonics

  return s

def songMyNoiseNet1Major():
  r1 = 30.0 * note.band(T=32, fx=note.frequency(note.Cs(2)))
  h1 = 1.0 * generateMyNoiseSeq(notes=note.flat([ note.B(1), note.G(0),  note.D(1), note.A(1)])) # flat([B(1), G(0), D(1), A(1)]) # sharp([A(1), F(0), C(1), G(0)])
  h2 = 0.7 * generateMyNoiseSeq(notes=note.flat([note.Gb(1), note.B(1), note.Gb(1), note.E(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  h3 = 0.3 * generateMyNoiseSeq(notes=note.flat([ note.D(1), note.D(1),  note.A(1), note.Db(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  s = r1 + h1 + h2 + h3
  return s, "song.mynoise.net.1.major.wav"

def songMyNoiseNet1Minor():
  s = generateMyNoiseSeq(notes=note.sharp([note.C(1), note.Gs(0), note.Ds(1), note.G(0)]))
  return s, "song.mynoise.net.1.minor.wav"

def songMyNoiseNet2Minor():
  s = 1.0 * generateMyNoiseSeq(notes=[note.Db(1),note.Db(1),note.A(1),note.Cb(1)])
  s += 0.6 * generateMyNoiseSeq(notes=[note.Db(1),note.Db(1),note.Db(1),note.Eb(1)])
  s += 0.4 * generateMyNoiseSeq(notes=[note.Ab(2),note.Ab(2),note.Fb(1),note.Gb(1)])
  return s, "song.mynoise.net.2.minor.wav"

def songMyNoiseNet3Major():
  s = 1.0 * generateMyNoiseSeq(notes=note.flat([note.Gb(0),note.D(1),note.A(1),note.E(0)]))
  return s, "song.mynoise.net.3.major.wav"

# ----------------------

s, f = songMyNoiseNet1Major()
# s, f = songMyNoiseNet1Minor()

# s, f = songMyNoiseNet2Minor()
# s, f = songMyNoiseNet3Major()

# ----------------------

loop(s, f)

# ----------------------
