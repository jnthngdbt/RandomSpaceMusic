from constants import *
from note import *
from song import *

def plotSound(x):
  T = dt*len(x)
  t = getTimeDomain(T)

  plt.figure()

  plt.subplot(1,2,1)
  plt.plot(t, x, '.-', markersize=3, linewidth=1)
  plt.xlabel('time (s)')
  plt.ylabel('sound')

  f = np.fft.fftfreq(len(x), dt)
  F = np.fft.fft(x)

  plt.subplot(1,2,2)
  plt.plot(f, np.abs(F), '.-', markersize=3, linewidth=1)
  plt.xlabel('frequency (Hz)')
  plt.ylabel('amplitude')
  plt.title('FFT')

def testNoiseToneSignal():
  x = generateNoiseTone(T=0.1, fx=5000)
  return s, "test.noise.tone.wav"

def testHarmonics():
  s = generateNoiseToneSeq(notes=(0,12,24,36), Tk=2, Tf=2)
  return s, "test.harmonics.wav"

def testSong():
  notes = [9,5,0,7]
  Tk = 5
  s = 20 * generateNoiseToneSeq(notes=notes, Tk=Tk, Tf=2)
  s += generateNoise(T=len(notes)*Tk, fl=500)
  s = tamperSignal(s, 1)
  return s, "test.song.wav"

def testNoise():
  s = generateNoise(T=10, fl=500)
  s = tamperSignal(s, 2)
  return s, "test.noise.wav"

def testSignalTampering():
  s = generateNoiseTone(T=5, fx=700)
  s = tamperSignal(s, 2)
  return s, "test.tamper.wav"

def testKick():
  s = []
  for _ in np.arange(10):
    Tk = 0.05
    fk = getNoteFrequency(A(0))
    sk = generateSine(T=Tk, fx=fk)
    sk = tamperSignal(sk, Tk/2)
    s = np.concatenate((s, np.zeros(int(fs * 0.25))))
    s = np.concatenate((s, sk))
    s = np.concatenate((s, np.zeros(int(fs * 0.25))))

  return s, "test.kick.wav"
  

# ----------------------
s = None
f = ""

# s = testSong()
# s, f = testNoise()
# s = testHarmonics()
# s = testNoiseToneSignal()
# s = testSignalTampering()
s, f = testKick()
# ----------------------

# ----------------------
if s is not None:
  play(s, f)

  plotSound(s)
  plt.show()
# ----------------------


