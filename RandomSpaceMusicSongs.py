from RandomSpaceMusic import *

def generateMyNoiseSeq(notes):
  Tk = 8 # s, for each note
  Tf = Tk # s, time fading in and out

  notes = np.array(notes)
  s = 2 * generateSineSeq(notes=notes, Tk=Tk, Tf=Tf)
  s += 1 * generateSineSeq(notes=notes+octave, Tk=Tk, Tf=Tf) # harmonics

  return s

def songMyNoiseNet1Major():
  r1 = 30.0 * generateNoiseTone(T=32, fx=getNoteFrequency(Cs(2)))
  h1 = 1.0 * generateMyNoiseSeq(notes=flat([ B(1), G(0),  D(1), A(1)])) # flat([B(1), G(0), D(1), A(1)]) # sharp([A(1), F(0), C(1), G(0)])
  h2 = 0.7 * generateMyNoiseSeq(notes=flat([Gb(1), B(1), Gb(1), E(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  h3 = 0.3 * generateMyNoiseSeq(notes=flat([ D(1), D(1),  A(1), Db(1)])) # flat([Gb(1), G(1), Gb(1), E(1)]) # sharp([E(1), F(1), E(1), D(1)])
  f = "song.mynoise.net.1.major.wav"
  while (1):
    kr = 0.0
    k1 = 1.0 + kr*np.random.rand()
    k2 = 1.0 + kr*np.random.rand()
    k3 = 1.0 + kr*np.random.rand()
    kr1 = 1.0 + kr*np.random.rand()
    writeWav(kr1*r1 + k1*h1 + k2*h2 + k3*h3, f, volume=0.4)
    winsound.PlaySound(f, 0)

def songMyNoiseNet1Minor():
  s = generateMyNoiseSeq(notes=sharp([C(1), Gs(0), Ds(1), G(0)]))
  writeWav(s, "song.mynoise.net.1.minor.wav")

def songMyNoiseNet2Minor():
  # kr = 0.1
  f = "song.mynoise.net.2.minor.wav"
  while (1):
    # s = 30.0 * generateNoiseTone(T=32, fx=getNoteFrequency(Db(1)))
    # s += 10.0 * generateNoiseTone(T=32, fx=getNoteFrequency(Ab(2)))
    # s += 4 * generateNoiseTone(T=32, fx=getNoteFrequency(Db(3)))
    # s += 1 * generateNoiseTone(T=32, fx=getNoteFrequency(Fb(3)))
    s = 1.0 * generateMyNoiseSeq(notes=[Db(1),Db(1),A(1),Cb(1)])
    s += 0.6 * generateMyNoiseSeq(notes=[Db(1),Db(1),Db(1),Eb(1)])
    s += 0.4 * generateMyNoiseSeq(notes=[Ab(2),Ab(2),Fb(1),Gb(1)])
    # s += 0.4 * generateMyNoiseSeq(notes=[Fb(2),Fb(2),A(2),Cb(2)])
    # s += 10.0 * generateNoiseTone(T=32, fx=getNoteFrequency(Ab(2)))
    # s += 4 * generateNoiseTone(T=32, fx=getNoteFrequency(Db(3)))
    # s += 1 * generateNoiseTone(T=32, fx=getNoteFrequency(Fb(3)))
    # s += (1.0 + kr*np.random.rand()) * 1.0 * generateMyNoiseSeq(notes=flat([ D(1), A(1),  F(0), C(1)]))
    writeWav(s, f, volume=0.4)
    winsound.PlaySound(f, 0)
  writeWav(s, f)

def songMyNoiseNet3Major():
  f = "song.mynoise.net.3.major.wav"
  while (1):
    s = 1.0 * generateMyNoiseSeq(notes=flat([Gb(0),D(1),A(1),E(0)]))
    # s += 0.8 * generateMyNoiseSeq(notes=[Cs(1),Cs(1),Cs(1),Cs(1)])
    # s += 0.6 * generateMyNoiseSeq(notes=[Es(1),Fs(1),Es(1),Ds(1)])
    # n = list(Cs(4) * np.ones((4*8*8,)))
    # s += 0.2 * generateSineSeq(notes=n, Tk=1/8, Tf=1/8)
    writeWav(s, f, volume=0.4)
    winsound.PlaySound(f, 0)

def songSamUrai():
  f = "song.sam.urai.wav"
  s = generateNoise(T=2*60, fx=500)
  s = tamperSignal(s, 20)
  writeWav(s, f, volume=1.0)
  winsound.PlaySound(f, 0)

# ----------------------
# songMyNoiseNet1Major()
# songMyNoiseNet1Minor()

# songMyNoiseNet2Minor()
# songMyNoiseNet3Major()

songSamUrai()

# ----------------------

plt.show()
