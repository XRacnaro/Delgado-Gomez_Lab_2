import Cesar, RailFence
import hashlib
from Main_Encriptacion import HashTextoPlano, N_Cesar, NivelesRailFence #Se exporta el hash del texto plano y los niveles de Cesar y RailFence

TextoDescrifrar = open('mensajeseguro.txt','r+') #Txt que contiene el texto encriptado por 2 cifrados de sustitución
TextoEncriptado = TextoDescrifrar.readlines()[0]
TextoDescrifrar.close()


DescifrarRailFence = RailFence.Desencriptar(TextoEncriptado, NivelesRailFence) #Descrifrado por RailFence

DescifradoCesar = Cesar.Rot(-N_Cesar)(DescifrarRailFence) #Descifrado por Cesar

#Metodo para Hashear el texto descrifrado
HashTextoDescifrado = hashlib.md5()
textoAHashear = DescifradoCesar
HashTextoDescifrado.update(textoAHashear.encode())
HashTextoDescencriptado = HashTextoDescifrado.hexdigest()

#Validador si el hash del texto plano es el mismo que el texto descrifrado
if HashTextoPlano == HashTextoDescencriptado:
  
    print("El mensaje no ha sido modificado")
else:
    print("El mensaje ha sido adulterado")

