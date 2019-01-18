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

def testNoiseSignal():
  x = generateNoiseTone(T=0.1, fx=5000)
  plotSound(x)

def testSong():
  s = generateNoiseToneSeq(notes=(4,5,7,5,2), Tk=2)
  writeWav(s, "test.noise.wav")

# ----------------------
testSong()
testNoiseSignal()
# ----------------------

plt.show()