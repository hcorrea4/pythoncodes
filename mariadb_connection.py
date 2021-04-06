#importar modulos sql
import mariadb
import sys

#Conectar hacia MariaDB
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
    
#Obtener cursor
cur = conexion.cursor()
#Agregar Datos
sql_insertar = "INSERT INTO decoded_table (decoded_passwd,original_passwd) VALUES (%s,%s)"
sql_datos = ("PE#$)#879","Casa_123")
try:
    #Ejecutar el comando SQL
    cur.execute(sql_insertar,sql_datos)
    #Registrar cambios con commit
    conexion.commit()
except:
    #Hacer Rollback en caso de algun error
    conexion.rollback()
#Imprimir que los datos fueron ingresados correctamente
print("Datos ingresados correctamente")

#Mostrar Datos de una tabla en particular   
cur.execute("SELECT id_decoded_passwd,decoded_passwd FROM decoded_table")
#Imprimir Resultados
for (id_decoded_passwd,decoded_passwd) in cur:
    print(f"Id Constraseña desencriptada: {id_decoded_passwd}, Contraseña desencriptada: {decoded_passwd}")
#Cerrar Conexion
conexion.close()


