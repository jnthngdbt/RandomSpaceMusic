from note import *
from song import *

def songSamUrai():
  s = generateNoise(T=2*60, fl=500)
  s = tamperSignal(s, 20)
  return s, "song.sam.urai.wav"

s, f = songSamUrai()
play(s, f)
