# x20210310.samourai.py

import midi
import note
import chord
import track
import song

def songSamUrai():
  Tk = 6 # s, for each note
  Tf = Tk
  f0 = 1
  type = 'peak'

  notes = [1, 3, 5, 8, 10, 12, 15]
  amps  = [4, 4, 5, 3, 3 , 2 , 0.5 ]
  C = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Cs(f0 + 0), notes=notes, amps=amps)
  G = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Gs(f0 + 0), notes=notes, amps=amps)
  A = chord.minor(T=Tk, Tf=Tf, type=type, root=midi.As(f0 + 1), notes=notes, amps=amps)
  F = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Fs(f0 + 0), notes=notes, amps=amps)

  # C = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Cs(f0 + 1), notes=[1, 3, 5, 8, 10], amps=[2, 2, 3, 3, 1])
  # G = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Gs(f0 + 0), notes=[3, 5, 8, 10], amps=[1, 3, 3, 1])
  # A = chord.minor(T=Tk, Tf=Tf, type=type, root=midi.As(f0 + 1), notes=[1, 3, 5, 8, 10], amps=[1, 1, 2, 2, 1])
  # F = chord.major(T=Tk, Tf=Tf, type=type, root=midi.Fs(f0 + 0), notes=[5, 8, 10, 12], amps=[1, 3, 3, 1])

  s = []
  t = []

  # t = track.append(t, note.silent(T=Tf))

  t = track.riff(t, [C, G, A, F])
  t = track.riff(t, [C, G, A, F])
  t = track.riff(t, [A, G, C, F])
  t = track.riff(t, [A, G, C])

  t = track.append(t, note.silent(T=Tf)) # let the reverb die

  s = track.add(s, t)

  # t = []
  # t = track.add(t, 1. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(5)), q=10))
  # t = track.add(t, 5. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(4)), q=10))
  # t = track.add(t, 10. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(3)), q=10))
  # # t = track.add(t, 800. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(2)), q=8))
  # t = note.normalize(t)

  # s = track.add(s, .5* t)

  s = note.reverb(s, delay=40000, decay=0.4)

  return s, "song.sam.urai.wav"

s, f = songSamUrai()
song.play(s, f, volume=0.8)