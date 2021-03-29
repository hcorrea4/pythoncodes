import base64
    
   
def encript_passwd():
    passwd = input("Ingrese la contraseña a encriptar: ")
    encripted_passwd = passwd.encode("utf-8")
    encoded_passwd = base64.b64encode(encripted_passwd)
    print("Contraseña encriptada: ", encoded_passwd)
    opcion = input("Desea encriptar otra contraseña? s/n ")
    if opcion == "s":
        encript_passwd()
    elif opcion == "n":
        passwd_secure()
    elif opcion != "s" or opcion != "n": 
        print("Elija una opcion correcta")
        
def decript_passwd():
    passwd = input("Ingrese la contraseña a desencriptar: ")
    decripted_passwd = passwd.encode("utf-8")
    decoded_passwd = base64.b64decode(decripted_passwd)
    print("Contraseña desencriptada: ", decoded_passwd) 
    opcion = input("Desea desencriptar otra contraseña? s/n ")
    if opcion == "s":
        encript_passwd()
    elif opcion == "n":
        passwd_secure()
    elif opcion != "s" or opcion != "n":
        print("Elija una opcion correcta")
        
def passwd_secure():
    menu = input("""
----------------------Encriptador de contraseñas----------------------
Elija la opcion que desee:
1 - Encriptar Contraseña
2 - Desencriptar Contraseña
3 - Salir
Elija una opcion: """)
    salida = True
    while salida:
        try:
            if int(menu) == 1:       
                encript_passwd()
                break
            elif int(menu) == 2:       
                decript_passwd()
                break            
            elif int(menu) == 3:
                salida = input("Deseas salir? s/n ")
                if salida == "s":
                    salida = False
                    print("Gracias por su atencion")
                    break
                elif salida == "n":
                    salida = True
                    passwd_secure()
                    break
                else:
                    salida = True
                    print("Elija una opcion!")
                    break                  
            else:
                print("Elija una opcion disponible!")  
        except ValueError:
            print("Solo dispone de numeros! Seleccione correctamente!")
            passwd_secure()
passwd_secure()                



