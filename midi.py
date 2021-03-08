import numpy as np

from constants import *

def freq(k):
  d = 8 # 4
  return 2 ** (k/octave) * (440 / d)

def major(root=0, note=1): return number(root, note, scale=[0, 2, 4, 5, 7, 9, 11])
def minor(root=0, note=1): return number(root, note, scale=[0, 2, 3, 5, 7, 8, 10])

def number(root=0, note=1, scale=[0, 2, 4, 5, 7, 9, 11]):
  if note <= 0: raise NameError('Scale note must be > 0. E.g. 1 for root, 5 for fifth.')
  note = note - 1 # make it 0 based
  N = len(scale)
  rem = note % N
  div = int(note / N)
  return root + div * octave + scale[rem]

  #        || .|  | .|  | .|  | .|  | .|  |  | .|  |  | .|                                                                                           
# G-----22-23 24 25 26 27-28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# D-----17-18 19 20 21 22-23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# A-----12-13 14 15 16 17-18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# E-----07-08 09 10 11 12-13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# B-----02-03 04 05 06 07-08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#
# 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E  F  F# G  G#
# 0                                   1                                   2                                   3                                  
#
# G-----------------------------------------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------
# D--------------------------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15---------------------------------------------
# A-----------------------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------------------------------------
# E--------------------0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15---------------------------------------------------------------------------
# B-----0--1--2--3--4--5--6--7--8--9--10-11-12-13-14-15------------------------------------------------------------------------------------------

# A  = 12, As = 13, B = 14, C = 15, Cs = 16, D = 17, Ds = 18, E = 19, F = 20, Fs = 21, G = 22, Gs = 23
def A (i): return  0 + octave * i
def As(i): return  1 + octave * i
def B (i): return  2 + octave * i
def C (i): return  3 + octave * i
def Cs(i): return  4 + octave * i
def D (i): return  5 + octave * i
def Ds(i): return  6 + octave * i
def E (i): return  7 + octave * i
def F (i): return  8 + octave * i
def Fs(i): return  9 + octave * i
def G (i): return 10 + octave * i
def Gs(i): return 11 + octave * i

def Ab(i): return Gs(i-1)
def Bb(i): return As(i)
def Cb(i): return B(i)
def Db(i): return Cs(i)
def Eb(i): return Ds(i)
def Fb(i): return E(i)
def Gb(i): return Fs(i)

def Bs(i): return C(i)
def Es(i): return F(i)

def sharp(notes): return np.array(notes) + 1
def flat(notes): return np.array(notes) - 1