import Cesar, RailFence
import hashlib

TextoACifrar = open('mensajedeentrada.txt','r+') #Txt que contiene el texto plano
TextoPlano = TextoACifrar.readlines()[0]
TextoACifrar.close()
TextoHash = hashlib.md5()
textoAHashear = TextoPlano
TextoHash.update(textoAHashear.encode())
HashTextoPlano = TextoHash.hexdigest()


N_Cesar = 5 #Nro de veces de Cesar
NivelesRailFence = 3 #Nro de bajas en Rail Fence


TextoCesar = Cesar.Rot(N_Cesar)(TextoPlano) #Texto cifrado con Cesar

TextoRailFence = RailFence.Encriptar(TextoCesar, NivelesRailFence)

archivoHashear = open('mensajeseguro.txt','w')
archivoHashear.write(TextoRailFence)
archivoHashear.close()

archivoTextoEncriptado = open('mensajeseguro.txt','r')
TextoEncriptado = archivoTextoEncriptado.readlines()
