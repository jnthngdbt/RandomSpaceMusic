from RandomSpaceMusic import *

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
  plotSound(x)

def testHarmonics():
  s = generateNoiseToneSeq(notes=(0,12,24,36), Tk=2, Tf=2)
  writeWav(s, "test.harmonics.wav")

def testSong():
  notes = [9,5,0,7]
  Tk = 5
  s = 20 * generateNoiseToneSeq(notes=notes, Tk=Tk, Tf=2)
  s += generateNoise(T=len(notes)*Tk, fx=500)
  s = tamperSignal(s, 1)
  writeWav(s, "test.song.wav")

def testNoise():
  s = generateNoise(T=10, fx=500)
  s = tamperSignal(s, 2)
  writeWav(s, "test.noise.wav")

def testSignalTampering():
  s = generateNoiseTone(T=5, fx=700)
  s = tamperSignal(s, 2)
  plotSound(s)
  writeWav(s, "test.tamper.wav")

# ----------------------
testSong()
# testNoise()
# testHarmonics()
# testNoiseToneSignal()
# testSignalTampering()
# ----------------------

plt.show()
