fs = 44100 # Hz, WAV file sampling frequency
dt = 1/fs # sec
nyquist = fs/2 # Hz
octave = 12

scales = {
  "major": [0, 2, 4, 5, 7, 9, 11],
  "minor": [0, 2, 3, 5, 7, 8, 10],
}