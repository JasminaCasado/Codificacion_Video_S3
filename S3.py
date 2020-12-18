import os


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def video_change_format():
    codecs = ["vp8", "vp9", "hevc"]
    resolutions = ["160", "360", "480", "720"]

    for codec in codecs:
        for resolution in resolutions:
            command = 'ffmpeg -i bbb_'+ resolution+'.mp4 -c:v ' + codec + ' bbb_'+ resolution + '_'+ codec+'.mkv'
            #print(command)
            os.system(command)

def streaming(video_stream):
    command = 'ffmpeg -re -i ' + video_stream + ' -an -c:v copy -f mpegts udp://@127.0.0.1:1234'
    #print(command)

    os.system(command)


salir = False
opcion = 0

while not salir:

    print ("1. Opcion 1 : Convertir Videos BBB")
    print ("2. Opcion 2 : Crear Streaming")
    print ("3. Salir")


    opcion = pedirNumeroEntero()

    if opcion == 1:
        video_change_format()

    elif opcion == 2:
        video_stream = input("Introduce el nombre del video que quieres reproducir en Streaming")
        streaming(video_stream)

    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fin")



