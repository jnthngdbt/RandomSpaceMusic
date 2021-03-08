import midi
import note

def major(T=2, root=0, notes=[1,3,5,8]):
  s = note.silent(T)
  for n in notes:
    k = midi.major(root, n)
    f = midi.freq(k)
    s += note.sine(T, f)
  return s

def minor(T=2, root=0, notes=[1,3,5,8]):
  s = note.silent(T)
  for n in notes:
    k = midi.minor(root, n)
    f = midi.freq(k)
    s += note.sine(T, f)
  return s
  