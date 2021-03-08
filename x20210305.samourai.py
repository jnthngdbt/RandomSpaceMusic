import note
import song

def songSamUrai():
  s = note.noise(T=2*60, fl=500)
  s = note.tamper(s, 20)
  return s, "song.sam.urai.wav"

s, f = songSamUrai()
song.play(s, f)
