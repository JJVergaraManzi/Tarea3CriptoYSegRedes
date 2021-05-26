from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

# inicialización de los datos
textoPlano = 'EsteEsUnMensajeQueSeraEncriptado'
keys = '1b69b49d6997ad001b69b49d69b97d00'
iv   = "12345678123456781234123401972634"
ivHex =binascii.a2b_hex(iv)
#Keys a hexadecimal
keysHex = binascii.a2b_hex(keys)
#cifrado CFB
cifrado = AES.new(keysHex, AES.MODE_CFB, iv= ivHex)

#Encriptacion
textoCifradoBytes =cifrado.encrypt(textoPlano.encode('utf-8'))
textoCifrado = binascii.b2a_base64(textoCifradoBytes).rstrip().decode('utf-8')
print("texto cifrado: " ,textoCifrado)

#Variables para html
textoCifradoHTML ='"'+textoCifrado+'"'
keysHTML = '"'+keys+'"'
ivHTML = '"'+iv+'"'

#Archivo html
html = open('index.html','w')
message = """<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tarea 3 Criptografia y seguridad en redes</title>
    </head>
    <body>
        <p>Este sitio contiene un mensaje secreto</p>
        <div class="AES" id="""+textoCifradoHTML+"""></div>
        <div class="keys" id="""+keysHTML+"""></div>
        <div class="iv" id="""+ivHTML+"""></div>
    </body>
</html>
"""
print(message)
html.write(message)
html.close()