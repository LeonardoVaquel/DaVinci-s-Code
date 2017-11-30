import stepic
from PIL import Image
from Encryptor import Encryptor, Decryptor

print "======================================================="
print "============= Bienvenido a DaVinci's Code ============="
print "======================================================="
print " "
print "ELIJA UNA OPCION DEPENDIENDO DE LO QUE QUIERA HACER"
opcion = 0
opcion = int(raw_input("OCULTAR UN MENSAJE = 1 , DEVELAR UN MENSAJE = 2 ") )


def encode_file(info, img):
    try:
        file = open(info, "r")
        contents = ""
        for string in file.readlines():
            contents = contents + string
    except Exception as e:
        print(e)
    return contents

def encode(info, img, tx, key):
    try:
        image = Image.open(img)
        contents = encode_file(tx, img)
        contents = contents + "*//*" + info
        encriptador = Encryptor()
        contents = encriptador.run(key, contents)
        st = stepic.encode(image, contents)
        name = img.split(".png")[0] + ".png"
        st.save(name, "png")
    except Exception as e:
        print(e)

def decode(img, key):
    desincriptador = Decryptor()
    image = Image.open(img)
    info = stepic.decode(image)
    info = desincriptador.run(key, info)
    file = open("result.txt", "w")
    file.write(info.split("*//*")[0])
    file.close()
    return info.split("*//*")[1]

if opcion == 1:
    mensaje= ""
    mensaje = str(raw_input("INGRESE EL MENSAJE QUE QUIERA OCULTAR: ") )
    tx = str(raw_input("INGRESE EL NOMBRE DEL ARCHIVO A OCULTAR: "))
    imagen = str(raw_input("INGRESE EL NOMBRE DE LA IMAGEN.PNG A OCULTAR: "))
    key = str(raw_input("INGRESE LA CLAVE PARA ENCRIPTAR: "))
    encode(mensaje, imagen, tx, key)
if opcion == 2:
    imagen = str(raw_input("INGRESE EL NOMBRE DE LA IMAGEN A DEVELAR: "))
    key = str(raw_input("INGRESE LA CLAVE PARA DESENCRIPTAR: "))
    messege = decode(imagen, key)
    print('DATOS OCULTOS: ')
    print (messege)
