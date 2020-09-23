import sqlite3
import os
import getpass 
import hashlib

conexion_wallapop = None
cursor_wallapop = None
try:
    conexion_wallapop = sqlite3.connect("wallapop.db")
    cursor_wallapop = conexion_wallapop.cursor()
    print (f"Conexión con la base de datos de productos establecidad correctamente. {conexion_wallapop}")
    print (f"Cursor establecido correctamente. {cursor_wallapop}")



except:
    print ("Error al conectarse a la base de datos de Wallapop.")


def encriptar(password):
    sh = hashlib.sha3_512()
    contraseña = password.encode() #PASA LA CONTRASEÑA A BYTES
    sh.update(contraseña) 
    password_encriptada = sh.hexdigest()
    return password_encriptada

def registrar():
    try:
        print ("Estableciendo conexión con la base de datos de usuarios.")
        conexion_database = sqlite3.connect("users.db")
        cursor_database = conexion_database.cursor()
    except:
        print ("Error conectandose a la base de datos de usuarios.")
    print ("CURSOR OK")


    usuario = str(input("User> "))
    password = getpass.getpass("Password> ")
    password_encriptada = encriptar(password)


    comando = f'INSERT INTO users(usuario,password) values("{usuario}","{password_encriptada}")'
    cursor_database.execute(comando)
    conexion_database.commit()
    print ("Usuario creado correctamente.")
        

        












def menu():
    print ("""
##### WALLAPOP 0.11 Admin Panel #####
    1. Ver productos. / Show Products
    2. Añadir productos / Add Product
    3. Eliminar productos. / Eliminate Product
    4. Registrar nueva cuenta / Register new account
    5. Guardar & salir. / Save & Exit
    """)
    opcion = int(input(">"))
    if opcion == 1:
        imprimir_productos()
    elif opcion == 2:
        insertar_producto()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        registrar()
    elif opcion == 5:
        print ("[#]Guardando cambios en la base de datos...")
        conexion_wallapop.commit()
        print ("[#]SALIENDO...")
        print ("[#]Base de datos guardada correctamente.")
    else:
        print ("[ERROR] No has seleccionado una opcion válida.")

def imprimir_productos():
    os.system("cls")
    print ("#############################################")
    cursor_wallapop.execute("SELECT * FROM wallapop")
    resultado = cursor_wallapop.fetchall()
    for x in resultado:
        print (f"[ID]",x[0],"[Producto]",x[1],"[Vendedor]",x[2])
    
    input("Presiona ENTER para continuar...")
    os.system("cls")    
    menu()

def eliminar_producto():
    os.system("cls")
    print ("#############################################")
    id_a_eliminar = int(input("Introduzca el ID del producto que desea eliminar >"))
    comando = f'DELETE FROM wallapop WHERE ID = {id_a_eliminar}'
    cursor_wallapop.execute(comando)
    print (f"Se ha eliminado el producto con ID --> {id_a_eliminar}")
    conexion_wallapop.commit()
    input("Presiona ENTER para continuar...")
    menu()


def insertar_producto():
    os.system("cls")
    producto = str(input("Nombre del producto>>"))
    vendedor = str(input("Nombre del vendedor>>"))
    #comando = """INSERT INTO wallapop(producto,vendedor,) values("test1","test2")"""
    comando = f'INSERT INTO wallapop(producto,vendedor) values("{producto}","{vendedor}")'
    #print (comando)
    cursor_wallapop.execute(comando)
    conexion_wallapop.commit()
    print (f"Se ha insertado correctamente [{producto}],[{vendedor}] ")
    input("Presiona ENTER para continuar...")
    os.system("cls")
    menu()

if __name__ == "__main__":
    menu()
