#Librerias importadas
import base64
import mariadb
import sys
#Banderas usadas
salida_menu = True

#Informacion de MariaDB
try:
    conexion = mariadb.connect(
        user = "hefesto",
        password = "hefesto",
        host = "192.168.1.69",
        port = 3306,
        database = "decode_encode_db"
    )
except mariadb.Error as error:
    print(f"Error de Conexion con MariaDB: {error}")
    sys.exit(1)

#Funciones (def)
#Añadir contraseñas desencriptadas a la base de datos
def add_decoded_to_db(passwd_original,deco_passwd):
    cursor = conexion.cursor()
    sql_insertar = "INSERT INTO decoded_table (decoded_passwd,original_passwd) VALUES (%s,%s)"
    sql_datos = (passwd_original,deco_passwd)
    try:
        #Ejecutar el comando SQL
        cursor.execute(sql_insertar,sql_datos)
        #Registrar cambios con commit
        conexion.commit()
    except:
        #Hacer Rollback en caso de algun error
        conexion.rollback()
    #Imprimir que los datos fueron ingresados correctamente
    print("Datos ingresados correctamente a la base de datos")

#Añadir contraseñas encriptadas a la base de datos
def add_encoded_to_db(passwd_original,enco_passwd):
    cursor = conexion.cursor()
    sql_insertar = "INSERT INTO encoded_table (original_passwd,encoded_passwd) VALUES (%s,%s)"
    sql_datos = (passwd_original,enco_passwd)
    try:
        #Ejecutar el comando SQL
        cursor.execute(sql_insertar,sql_datos)
        #Registrar cambios con commit
        conexion.commit()
    except:
        #Hacer Rollback en caso de algun error
        conexion.rollback()
    #Imprimir que los datos fueron ingresados correctamente
    print("Datos ingresados correctamente a la base de datos")
    
#Funcion para encriptar contraseña
def encript_passwd():
    salida = True
    while salida:
        passwd = input("Ingrese la contraseña a encriptar: ")
        encripted_passwd = passwd.encode("utf-8")
        encoded_passwd = base64.b64encode(encripted_passwd)
        print("Contraseña encriptada: ", encoded_passwd)
        add_encoded_to_db(passwd, encoded_passwd)
        opcion = input("Desea encriptar otra contraseña? s/n ")
        if opcion == "s":
            salida = True
        elif opcion == "n":
            salida = False
        elif opcion != "s" or opcion != "n": 
            print("Elija una opcion correcta")
#Funcion para desencriptar 
def decript_passwd():
    salida_decoded = True
    while salida_decoded:
        passwd_decode = input("Ingrese la contraseña a desencriptar: ")
        decripted_passwd = passwd_decode.encode("utf-8")
        decoded_passwd = base64.b64decode(decripted_passwd)
        print("Contraseña desencriptada: ", decoded_passwd)
        add_decoded_to_db(passwd_decode, decoded_passwd) 
        opcion = input("Desea desencriptar otra contraseña? s/n ")
        if opcion == "s":
            salida_decoded = True
        elif opcion == "n":
            salida_decoded = False
        elif opcion != "s" or opcion != "n":
            print("Elija una opcion correcta")

#Menu Principal
while salida_menu:
    menu = input("""
----------------------Encriptador y desencriptador de contraseñas----------------------
Elija la opcion que desee:
1 - Encriptar Contraseña
2 - Desencriptar Contraseña
3 - Ver Contraseñas Encriptadas
4 - Ver Contraseñas Desencriptadas
5 - Salir
Elija una opcion: """)
    try:
        if int(menu) == 1:       
            encript_passwd()
        elif int(menu) == 2:       
            decript_passwd()
        elif int(menu) == 3:
            #Obtener cursor
            cursor = conexion.cursor()
            #Mostrar Datos de una tabla en particular   
            cursor.execute("SELECT id_encoded,original_passwd,encoded_passwd FROM encoded_table")
            #Imprimir Resultados
            for (id_encoded,original_passwd,encoded_passwd) in cursor:
                print(f"Id Contraseña: {id_encoded}, Constraseña original: {original_passwd}, Contraseña encriptada: {encoded_passwd}")
        elif int(menu) == 4:
            #Obtener cursor
            cur = conexion.cursor()
            #Mostrar Datos de una tabla en particular   
            cur.execute("SELECT id_decoded_passwd,decoded_passwd FROM decoded_table")
            #Imprimir Resultados
            for (id_decoded_passwd,decoded_passwd) in cur:
                print(f"Id Constraseña desencriptada: {id_decoded_passwd}, Contraseña desencriptada: {decoded_passwd}")
            salida_menu = False
        elif int(menu) == 5:
            salida_opt = input("Deseas salir? s/n ")
            if salida_opt == "s":
                salida_menu = False
                print("Gracias por su atencion")
                break
            elif salida_opt == "n":
                salida_menu = True
            else:
                salida_menu = True
                print("Elija una opcion!")        
        else:   
            print("Elija una opcion disponible!")  
    except ValueError:
        print("Solo dispone de numeros! Seleccione correctamente!")
#Cerrar Conexion
conexion.close()
