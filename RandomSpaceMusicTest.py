from RandomSpaceMusic import *

def plotSound(x):
  T = dt*len(x)
  t = getTimeDomain(T)

  plt.figure()
  plt.plot(t, x, '.-', markersize=3, linewidth=1)
  plt.xlabel('time (s)')
  plt.ylabel('sound')

  f = np.fft.fftfreq(len(x), dt)
  F = np.fft.fft(x)

  plt.figure()
  plt.plot(f, np.real(F), '.-', markersize=3, linewidth=1)
  plt.xlabel('frequency (Hz)')
  plt.ylabel('amplitude')
  plt.title('FFT')

def testSong():
  s = generateNoiseToneSeq(notes=(4,5,7,5,2), Tk=2)
  writeWav(s, "test.noise.wav")
  plotSound(s)

testSong()

plt.show()
