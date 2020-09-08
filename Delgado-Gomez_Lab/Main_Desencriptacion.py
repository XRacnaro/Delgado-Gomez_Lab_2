import Cesar, RailFence
import hashlib
from Main_Encriptacion import HashTextoPlano

TextoACifrar = open('mensajeseguro.txt','r+') #Txt que contiene el texto plano
TextoPlano = TextoACifrar.readlines()[0]
TextoACifrar.close()

N_Cesar = 5 #Nro de veces de Cesar
NivelesRailFence = 3 #Nro de bajas en Rail Fence

TextoRailFence = RailFence.Desencriptar(TextoPlano, NivelesRailFence)

TextoCesar = Cesar.Rot(-N_Cesar)(TextoRailFence) #Texto cifrado con Cesar

TextoHash = hashlib.md5()
textoAHashear = TextoCesar
TextoHash.update(textoAHashear.encode())
HashTextoDecifrado = TextoHash.hexdigest()

if HashTextoPlano == HashTextoDecifrado:
    print("El mensaje no ha sido modificado")
else:
    print("El mensaje ha sido adulterado")

