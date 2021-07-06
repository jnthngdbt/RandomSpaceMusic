import numpy as np

import midi
import note
import chord
import track
import song
import utils

T = 0.08
Tf = 0.01
volume = 0.7

i = 0
song.play(note.sine(T=T, fx=midi.freq(midi.C(2)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.D(2)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.E(2)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.F(2)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.G(2)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.A(3)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.B(3)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1
song.play(note.sine(T=T, fx=midi.freq(midi.C(3)), Tf=Tf), "Beep." + str(i) + ".wav", volume=volume); i = i + 1