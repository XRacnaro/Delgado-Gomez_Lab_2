from string import ascii_lowercase as lc
from string import ascii_uppercase as uc

def Rot(n):
    Buscar = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(Buscar)
