import base64
def decode():
    salida = True
    print (salida)
    while salida:
        passwd = input("Ingrese la contraseña a encriptar: ")
        encripted_passwd = passwd.encode("utf-8")
        encoded_passwd = base64.b64encode(encripted_passwd)
        print("Contraseña encriptada: ", encoded_passwd)
        opcion = input("Desea encriptar otra contraseña? s/n ")
        if opcion == "s":
            salida = True
        elif opcion == "n":
            salida = False
        elif opcion != "s" or opcion != "n": 
            print("Elija una opcion correcta")
            


salida_menu = True
while salida_menu:
    menu = input("""Seleccione una opcion:
             1 - decode
             2 - salir 
             Elija una: """)
    if menu == "1":
        decode()
    elif menu == "2":
        salida_menu = False
        print("Gracias por su atencion")
    else:
        print("Escriba una opcion correcta!")
        salida_menu = True
        