# x20210310.samourai.py

import midi
import note
import chord
import track
import song

def songSamUrai():
  Tk = 8 # s, for each note
  Tf = Tk

  s = []
  t = []

  t = track.append(t, note.silent(T=Tf))

  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Cs(1), notes=[1, 3, 5, 8, 10], amps=[2, 2, 3, 3, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[3, 5, 8, 10], amps=[1, 3, 3, 1]))
  t = track.append(t, chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 3, 5, 8, 10], amps=[1, 1, 2, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Fs(0), notes=[5, 8, 10, 12], amps=[1, 3, 3, 1]))

  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Cs(1), notes=[1, 3, 5, 8, 10], amps=[2, 2, 3, 3, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[3, 5, 8, 10], amps=[1, 3, 3, 1]))
  t = track.append(t, chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 3, 5, 8, 10], amps=[1, 1, 2, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Fs(0), notes=[5, 8, 10, 12], amps=[1, 3, 3, 1]))

  t = track.append(t, chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 3, 5, 8, 10], amps=[1, 1, 2, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[3, 5, 8, 10], amps=[1, 3, 3, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Cs(1), notes=[1, 3, 5, 8, 10], amps=[2, 2, 3, 3, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Fs(0), notes=[5, 8, 10, 12], amps=[1, 3, 3, 1]))

  t = track.append(t, chord.minor(T=Tk, Tf=Tf, root=midi.As(1), notes=[1, 3, 5, 8, 10], amps=[1, 1, 2, 2, 1]))
  t = track.append(t, chord.major(T=Tk, Tf=Tf, root=midi.Gs(0), notes=[3, 5, 8, 10], amps=[1, 3, 3, 1]))

  t = track.append(t, chord.major(T=1.2*Tk, Tf=Tf, root=midi.Cs(1), notes=[1, 3, 5, 8], amps=[2, 2, 3, 3]))

  t = track.append(t, note.silent(T=Tf/2))

  s = track.add(s, t)
  t = []

  t = track.add(t, 100. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(4)), q=5))
  t = track.add(t, 800. * note.peak(T=note.duration(s), Tf=Tf, fx=midi.freq(midi.Cs(3)), q=8))

  s = track.add(s, 5.* t)

  return s, "song.sam.urai.wav"

s, f = songSamUrai()
song.play(s, f, volume=0.8)