import Cesar, RailFence
import hashlib

"""
Desafio:
Se le solicita a usted crear un programa el cual tenga como objetivo poder enviar un mensaje seguro
asegurando la integridad de este sin que este sea modificado, para esto se le pide a su equipo que
construya en el lenguaje que desee un programa que sea capas de cifrar ocupando cualquier red de
sustitucion que usted defina y generar un hash de un archivo de texto llamado mensajedeentrada.txt
generando un nuevo archivo llamado mensajeseguro.txt en el cual posteriormente puedan con un segundo
programa generar la operacion a la inversa, generando el mismo mensaje original con el adicional de
poder detectar si el mensaje ha sido modificado o no.
"""

Texto = "Hola Mundo ñoño"
Nivel_RF = 2

#Encriptado y desencriptado Cesar
Cesar_Encrypt = Cesar.Rot(3)(Texto)
print(Cesar_Encrypt)
print(Cesar.Rot(-3)(Cesar_Encrypt))

#Encriptado y desencriptado Rail Fence
RF_Encrypt = RailFence.Encriptar(Texto, Nivel_RF)
print(RF_Encrypt)
print(RailFence.Desencriptar(RF_Encrypt, Nivel_RF))

###############################################################

hashmd5 = hashlib.md5()    
stexto="hola Altaruru, hoy es lunes 1 de Octubre de 2018"
hashmd5.update(stexto.encode())
print (hashmd5.hexdigest())
