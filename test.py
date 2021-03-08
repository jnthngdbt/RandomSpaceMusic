
import matplotlib
import matplotlib.pyplot as plt

from constants import *
import midi
import note
import chord
import track
import song

matplotlib.style.use('dark_background')

def plotSound(x):
  T = dt*len(x)
  t = note.time(T)

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
  x = note.band(T=0.1, fx=5000)
  return s, "test.noise.tone.wav"

def testHarmonics():
  s = track.band(notes=(0,12,24,36), Tk=2, Tf=2)
  return s, "test.harmonics.wav"

def testSong():
  notes = [9,5,0,7]
  Tk = 5
  s = 20 * track.band(notes=notes, Tk=Tk, Tf=2)
  s += note.noise(T=len(notes)*Tk, fl=500)
  s = note.tamper(s, 1)
  return s, "test.song.wav"

def testNoise():
  s = note.noise(T=10, fl=500)
  s = note.tamper(s, 2)
  return s, "test.noise.wav"

def testSignalTampering():
  s = note.band(T=5, fx=700)
  s = note.tamper(s, 2)
  return s, "test.tamper.wav"

def testKick():
  s = []
  for _ in np.arange(10):
    Tk = 0.05
    fk = midi.freq(midi.A(0))
    sk = note.sine(T=Tk, fx=fk)
    sk = note.tamper(sk, Tk/2)
    s = np.concatenate((s, np.zeros(int(fs * 0.25))))
    s = np.concatenate((s, sk))
    s = np.concatenate((s, np.zeros(int(fs * 0.25))))

  return s, "test.kick.wav"

def testChordMajor():
  s = []
  s = chord.major(T=5, root=midi.F(1), notes=[1, 3, 5, 8])
  s = note.tamper(s, 1)
  return s, "test.chord.major.wav"

def testChordMinor():
  s = []
  s = chord.minor(T=5, root=midi.A(1), notes=[1, 3, 5, 8])
  s = note.tamper(s, 1)
  return s, "test.chord.minor.wav"

# ----------------------
# s, f = testSong()
# s, f = testNoise()
# s, f = testHarmonics()
# s, f = testNoiseToneSignal()
# s, f = testSignalTampering()
# s, f = testKick()
s, f = testChordMajor()
# s, f = testChordMinor()
# ----------------------
song.play(s, f)
# plotSound(s)
# plt.show()
# ----------------------


