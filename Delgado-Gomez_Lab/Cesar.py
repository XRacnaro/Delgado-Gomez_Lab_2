
#Se importam las letras mayusculas y minusculas ligadas al código ascci
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc

def Rot(n):
    Buscar = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n]) #Toma las letras pertenecientes a la oración o texto y las reposiciona por medio de operaciones
    return lambda s: s.translate(Buscar) #Pasa la palabra u oración de ascci a texto
