import pyodbc
import csv
from random import randint, uniform,random
import re
from clint.textui import colored
import os
import msvcrt
import time
#--------------------------------------------------------------------Creación de Base de datos---------------------------------------------------------------------------------------------------------#
# Este codigo fue construido utilizando el driver de oracle el cuál posee su propio administrador ODBC.

#Connection: Permite la conexión entre la base de datos y python, para poder conectar con una base de datos se deben reemplazar los parámetros de la función.
#El parámetro DSN debe igualarse al nombre del driver utilizado en su base de datos. Algunos drivers como el de oracle permite utilizar nombres personalizados.
#El parámetro DBQ debe igualarse al nombre de su base de datos
#El parámetro Uid debe igualarse al nombre de usuario de su base de datos, por defecto es SYSTEM
#El parámetro Pwd debe igualarse a la contraseña de la base de datos
print("Este programa utiliza la libreria PYODBC, para poder hacerlo funcionar correctamente se debe especificar los siguientes datos:\n ")
dsn=input("Ingrese el atributo DSN(Driver utilizado para la conexión entre la base de datos Oracle y python, algunos drivers como el de oracle permite nombres personalizados): ")
dbq=input("Ingrese el atributo DBQ(Suele ser el nombre de su bd): ")
uid=input("Ingrese el atributo UID(Usuario de su bd): ")
pwd=input("Ingrese el atributo PWD(Contraseña de su bd): ")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCargando los archivos .csv, esto puede tardar un tiempo......")
connection = pyodbc.connect('DSN='+dsn+';DBQ='+dbq+';Uid='+uid+';Pwd='+pwd+'')

#Se crea el cursor, el cual se utilizará para hacer las modificaciones de la base de datos.
cursor = connection.cursor()

def numeros(inputString):
    return any(char.isdigit() for char in inputString)

def create(cursor):
    random = randint(0,10)
    string="INSERT INTO tabla"
    print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInserte el nombre del Juego\n"))
    nombre=input()
    print(colored.cyan("\nInserte el genero del Juego\n"))
    genero = input()
    print(colored.cyan("\nInserte el desarrollador del Juego\n"))
    desarrollador = input()
    print(colored.cyan("\nInserte el publicador del Juego\n"))
    publicador = input()
    print(colored.cyan("\nInserte la fecha de estreno del Juego (FORMATO: Mes dia, año)\n"))
    fechadeestreno = input()
    print(colored.cyan("\nInserte SI o NO dependiendo de si el Juego es exclusivo o no\n"))
    exclusividad = input()
    print(colored.cyan("\nIngresar las valores en el siguiente orden:")+colored.yellow("\n Precio (Número)\n Stock (Número) \n Bodega (Número)")+colored.cyan("\nFavor de escribir cada valor seperado por un espacio\n"))
    (precio, stock , bodega)=input().split(" ")
    cursor.execute("INSERT INTO tabla (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, precio, stock , bodega, vendidos, ventasglobales, rating) values ('"+nombre+"','"+genero+"','"+desarrollador+"','"+publicador+"',TO_DATE('"+fechadeestreno+"', 'Month DD YYYY'),'"+exclusividad+"', "+precio+", "+str(stock)+", "+str(bodega)+", 0, 0, "+str(random)+")")
    flag=True
    global contadorinsert
    contadorinsert+=1
    cursor.commit()
    while(flag):
        print(colored.cyan("\nDesea insertar otro dato?\n1.-")+colored.yellow("Sí\n")+colored.cyan("2.-")+colored.yellow("No"))
        op=int(input())
        if(op==1):
            flag=False
            create(cursor)
        if(op==2):
            print(colored.cyan(contadorinsert), colored.cyan("rows han sido creadas\n"))
            print(colored.red("Presione cualquier tecla para continuar..."))
            c=msvcrt.getch()
            if(c):
                flag=False
        else:
            print("Opción Invalida, intentelo otra vez")

contadordelete=0;
def delete(cursor):
    global contadordelete
    string="DELETE FROM tabla WHERE "
    print(colored.cyan("Seleccione el tipo borrado que desea:\n1.-")+colored.yellow("Borrado por id\n")+colored.cyan("2.-")+colored.yellow("Borrado por Nombre\n")+colored.cyan("3.-")+colored.yellow("Borrado por desarrollador \n")+colored.cyan("4.-")+colored.yellow("Borrado por publicador\n")+colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese su opcion: "))
    condicion=int(input())
    if(condicion==1):
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese id: "))
        execute=input()
        cursor.execute(string+"id="+execute)
    if(condicion==2):
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese Nombre: "))
        execute=input()
        cursor.execute(string+"nombre="+"'"+execute+"'")
    if(condicion==3):
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese Desarrollador: "))
        execute=input()
        cursor.execute(string+"desarrollador="+"'"+execute+"'")
    if(condicion==4):
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese Publicador: "))
        execute=input()
        cursor.execute(string+"publicador="+"'"+execute+"'")
    flag=True


    cursor.commit()
    while(flag):
        contadordelete+=1
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDesea borrar otro dato?\n1.-")+colored.yellow("Sí")+colored.cyan("\n2.-")+colored.yellow("No"))
        op=int(input())
        if(op==1):
            flag=False
            delete(cursor)
        if(op==2):
            print(colored.cyan(contadordelete), colored.cyan("rows han sido borradas\n"))
            contadordelete=0
            print(colored.red("Presione cualquier tecla para continuar..."))
            c=msvcrt.getch()
            if(c):
                flag=False

def read(cursor):
    flag = True
    print(colored.cyan("Quieres leer todo el contenido?\n1.-")+colored.yellow("Si\n")+colored.cyan("2.-")+colored.yellow("No\n")+colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese su opción: "))
    pregunta = int(input())
    if(pregunta == 1):
        cursor.execute("SELECT * FROM tabla")
        print(colored.yellow("ID")+colored.cyan("|")+colored.yellow("Nombre del videojuego")+colored.cyan("|")+colored.yellow("Genero")+colored.cyan("|")+colored.yellow("Desarrollador")+colored.cyan("|")+colored.yellow("Publicadora")+colored.cyan("|")+colored.yellow("Exclusividad")+colored.cyan("|")+colored.yellow("Fecha de publicación")+colored.cyan("|")+colored.yellow("Precio")+colored.cyan("|")+colored.yellow("Stock")+colored.cyan("|")+colored.yellow("En Bodega")+colored.cyan("|")+colored.yellow("Ventas locales")+colored.cyan("|")+colored.yellow("Ventas globales")+colored.cyan("|")+colored.yellow("Rating"))
        for row in cursor:
            print(colored.yellow(str(row[0]))+colored.cyan("|")+colored.yellow(str(row[1]))+colored.cyan("|")+colored.yellow(str(row[2]))+colored.cyan("|")+colored.yellow(str(row[3]))+colored.cyan("|")+colored.yellow(str(row[4]))+colored.cyan("|")+colored.yellow(str(row[5]))+colored.cyan("|")+colored.yellow(str(row[6]))+colored.cyan("|")+colored.yellow(str(row[7]))+colored.cyan("|")+colored.yellow(str(row[8]))+colored.cyan("|")+colored.yellow(str(row[9]))+colored.cyan("|")+colored.yellow(str(row[10]))+colored.cyan("|")+colored.yellow(str(row[11])))
        print(colored.red("Presione cualquier tecla para continuar..."))
        c=msvcrt.getch()
        if(c):
            flag=False

    elif(pregunta == 2):
        print(colored.cyan("1.-")+colored.yellow("Leer lineas especificas\n")+colored.cyan("2.-")+colored.yellow("Leer hasta N linea\n")+colored.cyan("3.-")+colored.yellow("Leer desde N hasta M lineas\n")+colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese su opcion: "))
        pregunta = int(input())
        if(pregunta == 1):
            print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngresa la linea especifica que quieras leer (-1 para salir)"))
            while(flag):

                pregunta = int(input())
                if(pregunta != -1):
                    cursor.execute("SELECT * FROM tabla WHERE id="+str(pregunta)+"")

                    for row in cursor:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+colored.yellow("ID")+colored.cyan("|")+colored.yellow("Nombre del videojuego")+colored.cyan("|")+colored.yellow("Genero")+colored.cyan("|")+colored.yellow("Desarrollador")+colored.cyan("|")+colored.yellow("Publicadora")+colored.cyan("|")+colored.yellow("Exclusividad")+colored.cyan("|")+colored.yellow("Fecha de publicación")+colored.cyan("|")+colored.yellow("Precio")+colored.cyan("|")+colored.yellow("Stock")+colored.cyan("|")+colored.yellow("En Bodega")+colored.cyan("|")+colored.yellow("Ventas locales")+colored.cyan("|")+colored.yellow("Ventas globales")+colored.cyan("|")+colored.yellow("Rating"))
                        print(colored.yellow(str(row[0]))+colored.cyan("|")+colored.yellow(str(row[1]))+colored.cyan("|")+colored.yellow(str(row[2]))+colored.cyan("|")+colored.yellow(str(row[3]))+colored.cyan("|")+colored.yellow(str(row[4]))+colored.cyan("|")+colored.yellow(str(row[5]))+colored.cyan("|")+colored.yellow(str(row[6]))+colored.cyan("|")+colored.yellow(str(row[7]))+colored.cyan("|")+colored.yellow(str(row[8]))+colored.cyan("|")+colored.yellow(str(row[9]))+colored.cyan("|")+colored.yellow(str(row[10]))+colored.cyan("|")+colored.yellow(str(row[11]))+"\n")
                else:
                    flag=False
        elif(pregunta == 2):
            print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHasta que linea quieres leer?"))
            pregunta = int(input())
            cursor.execute("SELECT * FROM tabla WHERE id<="+str(pregunta)+"")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+colored.yellow("ID")+colored.cyan("|")+colored.yellow("Nombre del videojuego")+colored.cyan("|")+colored.yellow("Genero")+colored.cyan("|")+colored.yellow("Desarrollador")+colored.cyan("|")+colored.yellow("Publicadora")+colored.cyan("|")+colored.yellow("Exclusividad")+colored.cyan("|")+colored.yellow("Fecha de publicación")+colored.cyan("|")+colored.yellow("Precio")+colored.cyan("|")+colored.yellow("Stock")+colored.cyan("|")+colored.yellow("En Bodega")+colored.cyan("|")+colored.yellow("Ventas locales")+colored.cyan("|")+colored.yellow("Ventas globales")+colored.cyan("|")+colored.yellow("Rating"))
            for row in cursor:
                print(colored.yellow(str(row[0]))+colored.cyan("|")+colored.yellow(str(row[1]))+colored.cyan("|")+colored.yellow(str(row[2]))+colored.cyan("|")+colored.yellow(str(row[3]))+colored.cyan("|")+colored.yellow(str(row[4]))+colored.cyan("|")+colored.yellow(str(row[5]))+colored.cyan("|")+colored.yellow(str(row[6]))+colored.cyan("|")+colored.yellow(str(row[7]))+colored.cyan("|")+colored.yellow(str(row[8]))+colored.cyan("|")+colored.yellow(str(row[9]))+colored.cyan("|")+colored.yellow(str(row[10]))+colored.cyan("|")+colored.yellow(str(row[11])))
            print(colored.red("Presione cualquier tecla para continuar..."))
            c=msvcrt.getch()
            if(c):
                flag=False
        elif(pregunta == 3):
            print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInserte la linea de inicio"))
            pregunta = int(input())
            print(colored.cyan("Inserte la ultima linea"))
            pregunta2 = int(input())
            cursor.execute("SELECT * FROM tabla WHERE id BETWEEN "+str(pregunta)+" AND "+str(pregunta2)+"")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+colored.yellow("ID")+colored.cyan("|")+colored.yellow("Nombre del videojuego")+colored.cyan("|")+colored.yellow("Genero")+colored.cyan("|")+colored.yellow("Desarrollador")+colored.cyan("|")+colored.yellow("Publicadora")+colored.cyan("|")+colored.yellow("Exclusividad")+colored.cyan("|")+colored.yellow("Fecha de publicación")+colored.cyan("|")+colored.yellow("Precio")+colored.cyan("|")+colored.yellow("Stock")+colored.cyan("|")+colored.yellow("En Bodega")+colored.cyan("|")+colored.yellow("Ventas locales")+colored.cyan("|")+colored.yellow("Ventas globales")+colored.cyan("|")+colored.yellow("Rating"))
            for row in cursor:
                print(colored.yellow(str(row[0]))+colored.cyan("|")+colored.yellow(str(row[1]))+colored.cyan("|")+colored.yellow(str(row[2]))+colored.cyan("|")+colored.yellow(str(row[3]))+colored.cyan("|")+colored.yellow(str(row[4]))+colored.cyan("|")+colored.yellow(str(row[5]))+colored.cyan("|")+colored.yellow(str(row[6]))+colored.cyan("|")+colored.yellow(str(row[7]))+colored.cyan("|")+colored.yellow(str(row[8]))+colored.cyan("|")+colored.yellow(str(row[9]))+colored.cyan("|")+colored.yellow(str(row[10]))+colored.cyan("|")+colored.yellow(str(row[11])))
            print(colored.red("Presione cualquier tecla para continuar..."))
            c=msvcrt.getch()
            if(c):
                flag=False
def update(cursor):
    flag = True
    print(colored.cyan("--------------------------------------------------------------------\n|")+colored.yellow("Inserte la ID o Nombre del juego que quieres editar (0) para salir")+colored.cyan("|\n--------------------------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
    dato = input()
    try:
        dato = int(dato)
        if(dato != 0):
            while(flag):
                print(colored.cyan("¿Que quieres modificar?\n1.-")+colored.yellow("Aceptar cambios\n")+colored.cyan("2.-")+colored.yellow("Cancelar Cambios\n")+colored.cyan("3.-")+colored.yellow("Nombre\n")+colored.cyan("4.-")+colored.yellow("Genero\n")+colored.cyan("5.-")+colored.yellow("Desarrollador\n")+colored.cyan("6.-")+colored.yellow("Publicador\n")+colored.cyan("7.-")+colored.yellow("Fecha de estreno\n")+colored.cyan("8.-")+colored.yellow("Exclusividad\n")+colored.cyan("9.-")+colored.yellow("Precio\n")+colored.cyan("10.-")+colored.yellow("Stock\n")+colored.cyan("11.-")+colored.yellow("Bodega\n")+colored.cyan("12.-")+colored.yellow("Cantidad Vendidos Local\n")+colored.cyan("13.-")+colored.yellow("Cantidad Vendidos Global\n")+colored.cyan("14.-")+colored.yellow("Rating\n")+colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese su opción: "))
                pregunta = int(input())
                if(pregunta == 1):
                    try:
                        cursor.commit()
                        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLos datos han sido modificados correctamente"))
                        time.sleep(3)
                        update(cursor)
                        flag = False
                    except:
                        print("#ERROR: Informar al administrador de la base de datos")
                        time.sleep(5)
                        update(cursor)
                        flag = False
                if(pregunta == 2):
                    cursor.rollback()
                    print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNo se ha guardado ningun cambio"))
                    time.sleep(3)
                    update(cursor)
                    flag = False
                if(pregunta>2):
                    print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngresa la modificacion que quieres hacer: "))
                    preguntados = input()
                if(pregunta==3):
                    cursor.execute("update tabla SET nombre='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==4):
                    cursor.execute("update tabla SET genero='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==5):
                    cursor.execute("update tabla SET desarrollador='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==6):
                    cursor.execute("update tabla SET publicador='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==7):
                    cursor.execute("update tabla SET fechadeestreno=TO_DATE('"+preguntados+"','Month DD YYYY') WHERE id="+str(dato)+"")
                elif(pregunta==8):
                    cursor.execute("update tabla SET exclusividad='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==9):
                    cursor.execute("update tabla SET precio='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==10):
                    cursor.execute("update tabla SET stock='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                    if(int(preguntados) < 10):
                        bodega=10-int(preguntados)
                        print("ADVERTENCIA: EL STOCK HA LLEGADO A SU LÍMITE DE MENOS DE 10 UNIDADES, SE DEBEN DE SACAR "+str(bodega)+" EXISTENCIAS DE LA BODEGA COMO MÍNIMO, LA BASE DE DATOS SE ACTUALIZARÁ AUTOMATICAMENTE CON EL MÍNIMO INDICADO DESCONTANDOLO DE LA BODEGA.\n")
                elif(pregunta==11):
                    cursor.execute("update tabla SET bodega='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==12):
                    cursor.execute("update tabla SET vendidos='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==13):
                    cursor.execute("update tabla SET ventasglobales='"+str(preguntados)+"' WHERE id="+str(dato)+"")
                elif(pregunta==14):
                    cursor.execute("update tabla SET rating='"+str(preguntados)+"' WHERE id="+str(dato)+"")
    except:
        while(flag):
            print(colored.cyan("¿Que quieres modificar?\n1.-")+colored.yellow("Aceptar cambios\n")+colored.cyan("2.-")+colored.yellow("Cancelar Cambios\n")+colored.cyan("3.-")+colored.yellow("Nombre\n")+colored.cyan("4.-")+colored.yellow("Genero\n")+colored.cyan("5.-")+colored.yellow("Desarrollador\n")+colored.cyan("6.-")+colored.yellow("Publicador\n")+colored.cyan("7.-")+colored.yellow("Fecha de estreno\n")+colored.cyan("8.-")+colored.yellow("Exclusividad\n")+colored.cyan("9.-")+colored.yellow("Precio\n")+colored.cyan("10.-")+colored.yellow("Stock\n")+colored.cyan("11.-")+colored.yellow("Bodega\n")+colored.cyan("12.-")+colored.yellow("Cantidad Vendidos Local\n")+colored.cyan("13.-")+colored.yellow("Cantidad Vendidos Global\n")+colored.cyan("14.-")+colored.yellow("Rating\n")+colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\nIngrese su opción: "))
            pregunta = int(input())
            if(pregunta == 1):
                try:
                    cursor.commit()
                    print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLos datos han sido modificados correctamente"))
                    time.sleep(3)
                    update(cursor)
                    flag = False
                except:
                    print("#ERROR: Informar al administrador de la base de datos")
                    time.sleep(5)
                    update(cursor)
                    flag = False
            if(pregunta == 2):
                cursor.rollback()
                print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNo se ha guardado ningun cambio"))
                time.sleep(3)
                update(cursor)
                flag = False
            if(pregunta>2):
                print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIngresa la modificacion que quieres hacer: "))
                preguntados = input()
            if(pregunta==3):
                cursor.execute("update tabla SET nombre='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==4):
                cursor.execute("update tabla SET genero='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==5):
                cursor.execute("update tabla SET desarrollador='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==6):
                cursor.execute("update tabla SET publicador='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==7):
                cursor.execute("update tabla SET fechadeestreno=TO_DATE('"+preguntados+"','Month DD YYYY') WHERE id="+str(dato)+"")
            elif(pregunta==8):
                cursor.execute("update tabla SET exclusividad='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==9):
                cursor.execute("update tabla SET precio='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==10):
                cursor.execute("update tabla SET stock='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==11):
                cursor.execute("update tabla SET bodega='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==12):
                cursor.execute("update tabla SET vendidos='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==13):
                cursor.execute("update tabla SET ventasglobales='"+str(preguntados)+"' WHERE id="+str(dato)+"")
            elif(pregunta==14):
                cursor.execute("update tabla SET rating='"+str(preguntados)+"' WHERE id="+str(dato)+"")




#--------------------------------------------------------------------------------------CONSULTAS PEDIDAS ESPECÍFICAMENTE EN LA TAREA-------------------------------------------------------------------#
def cincoexclusivos(cursor):
    menuflag=False
    print(colored.cyan("-----------------------------------\n|")+colored.yellow("Cinco juegos exclusivos mas caros")+colored.cyan("|\n-----------------------------------"))
    cursor.execute("""SELECT * FROM cincoexclusivos;""")

    for row in cursor:
        print(colored.cyan("Juego:"),colored.yellow(row[0]),"\n",colored.cyan("Genero:"),colored.yellow(row[1]),"\n",colored.cyan("Desarrollador:"),colored.yellow(row[2]),"\n",colored.cyan("Publicador:"),colored.yellow(row[3]),"\n",colored.cyan("Precio:"),colored.yellow(row[4]),colored.yellow("Dolares"))
    print(colored.red("Presione cualquier tecla para continuar..."))

    if(msvcrt.getch()):
        menuflag=True



def masvendidos(cursor):
    menuflag=False
    cursor.execute("""SELECT * FROM masvendidosuno;""")
    print(colored.cyan("----------------------------------\n|")+colored.yellow("Tres juegos mas vendidos locales")+colored.cyan("|\n----------------------------------"))
    for row in cursor:
        print(colored.cyan("Juego:"),colored.yellow(row[0]),"\n",colored.cyan("Genero:"),colored.yellow(row[1]),"\n",colored.cyan("Desarrollador:"),colored.yellow(row[2]),"\n",colored.cyan("Publicador:"),colored.yellow(row[3]),"\n",colored.cyan("Vendidos:"),colored.yellow(row[4]),colored.yellow("Copias\n"))
    print(colored.red("\n\n\n\n\n\n\nPresione cualquier tecla para continuar..."))
    b=msvcrt.getch()
    if(b):
        cursor.execute("""SELECT * FROM masvendidos""")
        print(colored.cyan("-----------------------------------\n|")+colored.yellow("Tres juegos mas vendidos globales")+colored.cyan("|\n-----------------------------------"))
        for row in cursor:
            print(colored.cyan("Juego:"),colored.yellow(row[0]),"\n",colored.cyan("Genero:"),colored.yellow(row[1]),"\n",colored.cyan("Desarrollador:"),colored.yellow(row[2]),"\n",colored.cyan("Publicador:"),colored.yellow(row[3]),"\n",colored.cyan("Vendidos:"),colored.yellow(row[4]),colored.yellow("Copias\n"))
        print(colored.red("\n\n\n\n\n\n\nPresione cualquier tecla para continuar..."))
        time.sleep(1)
        c=msvcrt.getch()
        if(c):
            menuflag=True

def desarrolladorasventas(cursor):
    menuflag=False
    print(colored.cyan("--------------------------------------------\n|")+colored.yellow("Tres Desarolladoras con mas ventas locales")+colored.cyan("|\n--------------------------------------------"))
    cursor.execute("""SELECT * FROM desarrollador""")
    for row in cursor:
        print(colored.cyan("Desarollador:"),colored.yellow(row[0]),"\n",colored.cyan("Ventas locales:"),colored.yellow(row[1]),colored.yellow("Copias\n"))
    print(colored.red("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPresione cualquier tecla para continuar..."))
    b=msvcrt.getch()
    if(b):
        menuflag=True

def rating(cursor):
    menuflag=False
    print(colored.cyan("---------------------------\n|")+colored.yellow("Tres Juegos con Mejores Rating")+colored.cyan("|\n---------------------------"))
    cursor.execute("""SELECT * FROM rating""")
    for row in cursor:
        print(colored.cyan("Juego:"),colored.yellow(row[0]),"\n",colored.cyan("Rating:"),colored.yellow(row[1]),"\n",colored.cyan("Fecha de Lanzamiento:"),colored.yellow(row[2]))
    print(colored.red("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPresione cualquier tecla para continuar..."))
    b=msvcrt.getch()
    if(b):
        menuflag=True




#Se crea la tabla de Sansanoplay y de Nintendo, se elige las id de ambas tablas como claves Primarias.
tablauno = """CREATE TABLE SansanoPlay
(
id INTEGER,
nombre varchar2(250),
precio INTEGER,
stock INTEGER,
bodega INTEGER,
vendidos INTEGER,
PRIMARY KEY (id)
)"""
string2 = "CREATE TABLE Nintendo(id integer, nombre varchar(100), genero varchar(100), desarrollador varchar(100),publicador varchar(100),fechadeestreno date,exclusividad varchar(3),ventasglobales integer,rating integer,primary key (id))"
cursor.execute("DROP TABLE Nintendo")
cursor.execute("DROP TABLE SansanoPlay")
cursor.execute(string2)
cursor.execute(tablauno)

#Se realizan dos triggers. Ambos triggers tienen la función de que cada vez que se añada un elemento a una tabla, va a tener una id única y distinta.
#Para lograr esto, se crea una secuencia que aumenta su valor cada vez que se inserta un elemento con id.

cursor.execute("DROP SEQUENCE Secuencia2")
cursor.execute("CREATE SEQUENCE Secuencia2")
cursor.execute("""CREATE TRIGGER Nintendo
BEFORE INSERT ON SYSTEM.Nintendo
FOR EACH ROW
BEGIN
  SELECT Secuencia2.nextval
  INTO :new.id
  FROM dual;
END;""")
cursor.execute("DROP SEQUENCE Secuencia")
cursor.execute("CREATE SEQUENCE Secuencia")
cursor.execute("""CREATE TRIGGER SansanoPlay
BEFORE INSERT ON SYSTEM.SansanoPlay
FOR EACH ROW
BEGIN
  SELECT Secuencia.nextval
  INTO :new.id
  FROM dual;
END;""")

#Se crea una vista que representa la unión entre la tabla de sansanoPlay y la tabla Nintendo.

cursor.execute("""CREATE OR REPLACE VIEW tabla AS
SELECT SansanoPlay.id, SansanoPlay.nombre, Nintendo.genero, Nintendo.desarrollador, Nintendo.publicador, Nintendo.fechadeestreno, Nintendo.exclusividad, SansanoPlay.precio, SansanoPlay.stock, SansanoPlay.bodega, SansanoPlay.vendidos, Nintendo.ventasglobales, Nintendo.rating
FROM SansanoPlay
INNER JOIN Nintendo
ON SansanoPlay.id = Nintendo.id""")


#Se realiza un trigger que se activa cada vez que se modifica la view. Modifica los datos en las tablas por separado.
cursor.execute("""CREATE OR REPLACE TRIGGER triggerview
INSTEAD OF INSERT ON tabla
FOR EACH ROW
BEGIN
 INSERT INTO SansanoPlay (nombre, precio, stock, bodega, vendidos) VALUES (:new.nombre,:new.precio,:new.stock,:new.bodega,:new.vendidos);
 INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) VALUES (:new.nombre,:new.genero,:new.desarrollador,:new.publicador,:new.fechadeestreno,:new.exclusividad,:new.ventasglobales,:new.rating);
END;""")
cursor.execute("""CREATE OR REPLACE VIEW rating AS SELECT nombre,rating,fechadeestreno FROM (SELECT nombre,rating,fechadeestreno FROM tabla ORDER BY rating DESC, TO_CHAR(fechadeestreno, 'YYYY-MM-DD') DESC) WHERE ROWNUM <=3;""")
cursor.execute("""CREATE OR REPLACE VIEW masvendidosuno AS SELECT nombre, genero, desarrollador, publicador, vendidos FROM (SELECT nombre, genero, desarrollador, publicador, vendidos FROM tabla ORDER BY vendidos DESC) WHERE ROWNUM <=3;""")
cursor.execute("""CREATE OR REPLACE VIEW masvendidos AS SELECT nombre, genero, desarrollador, publicador, ventasglobales FROM (SELECT nombre, genero, desarrollador, publicador, ventasglobales FROM tabla ORDER BY ventasglobales DESC) WHERE ROWNUM <=3;""")
cursor.execute("""CREATE OR REPLACE VIEW cincoexclusivos AS SELECT nombre, genero, desarrollador, publicador, precio FROM (SELECT nombre, genero, desarrollador, publicador, precio FROM tabla WHERE exclusividad='Si' ORDER BY precio DESC) WHERE ROWNUM <=5""")

cursor.execute("""CREATE OR REPLACE VIEW desarrollador AS SELECT * FROM (SELECT desarrollador,SUM(vendidos) FROM tabla GROUP BY desarrollador ORDER BY SUM(vendidos) DESC) WHERE ROWNUM <=3""")


#
with open(r"Sansanoplay.csv", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    entero = 5
    for row in csv_reader:
        if i!=0:
            random = randint(5,120)
            random2 = randint(0,10000)
            random3 = randint(0,10000)
            random4 = randint(0,10000)
            try:
                cursor.execute("INSERT INTO SansanoPlay (nombre, precio, stock, bodega, vendidos) values (q'<"+row[1]+">', "+str(random)+", "+str(random2)+", "+str(random3)+", "+str(random4)+")")
            except:
                cursor.execute("INSERT INTO SansanoPlay (nombre, precio, stock, bodega, vendidos) values (q''"+row[1]+"'', "+str(random)+", "+str(random2)+", "+str(random3)+", "+str(random4)+")")
            connection.commit()
        i+=1


with open(r"Nintendo.csv") as File:
    reader = csv.reader(File)
    i=0
    lista = []
    for row in reader:
        fecha = ''
        if("January" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("January", "Enero")
        elif("February" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("February", "Febrero")
        elif("March" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("March", "Marzo")
        elif("April" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("April", "Abril")
        elif("May" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("May", "Mayo")
        elif("June" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("June", "Junio")
        elif("July" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("July", "Julio")
        elif("August" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("August", "Agosto")
        elif("September" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("September", "Septiembre")
        elif("October" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("October", "Octubre")
        elif("November" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("November", "Noviembre")
        elif("December" in row[5] and numeros(row[5]) and "," in row[5]):
            fecha = row[5].replace("December", "Diciembre")
        elif("," not in row[5] and "Q1" not in row[5] and "Q2" not in row[5] and "Q3" not in row[5] and "Q4" not in row[5]):
            lista = row[5].split(" ")
            if("January" in lista[0]):
                lista[0] = lista[0].replace("January", "Enero")
                fecha = lista[0]+" 1, "+lista[1]
            elif("February" in lista[0]):
                lista[0] = lista[0].replace("February", "Febrero")
                fecha = lista[0]+" 1, "+lista[1]
            elif("March" in lista[0]):
                lista[0] = lista[0].replace("March", "Marzo")
                fecha = lista[0]+" 1, "+lista[1]
            elif("April" in lista[0]):
                lista[0] = lista[0].replace("April", "Abril")
                fecha = lista[0]+" 1, "+lista[1]
            elif("May" in lista[0]):
                lista[0] = lista[0].replace("May", "Mayo")
                fecha = lista[0]+" 1, "+lista[1]
            elif("June" in lista[0]):
                lista[0] = lista[0].replace("June", "Junio")
                fecha = lista[0]+" 1, "+lista[1]
            elif("July" in lista[0]):
                lista[0] = lista[0].replace("July", "Julio")
                fecha = lista[0]+" 1, "+lista[1]
            elif("August" in lista[0]):
                lista[0] = lista[0].replace("August", "Agosto")
                fecha = lista[0]+" 1, "+lista[1]
            elif("September" in lista[0]):
                lista[0] = lista[0].replace("September", "Septiembre")
                fecha = lista[0]+" 1, "+lista[1]
            elif("October" in lista[0]):
                lista[0] = lista[0].replace("October", "Octubre")
                fecha = lista[0]+" 1, "+lista[1]
            elif("November" in lista[0]):
                lista[0] = lista[0].replace("November", "Noviembre")
                fecha = lista[0]+" 1, "+lista[1]
            elif("December" in lista[0]):
                lista[0] = lista[0].replace("December", "Diciembre")
                fecha = lista[0]+" 1, "+lista[1]
            else:
                fecha = lista[0]+" 31, "+lista[1]
        elif("Q1" in row[5]):
            fecha = "Marzo 1, 2020"
        elif("Q2" in row[5]):
            fecha = "Julio 1, 2020"
        elif("Q3" in row[5]):
            fecha = "Septiembre 1, 2020"
        elif("Q4" in row[5]):
            fecha = "Diciembre 1, 2020"
        random = randint(0,10000)
        random2 = randint(0, 100)
        if i!=0:
            try:
                cursor.execute("INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) values (q'<"+row[1]+">', q'<"+row[2]+">', q'<"+row[3]+">', q'<"+row[4]+">', TO_DATE('"+fecha+"','Month DD YYYY'), q'<"+row[6]+">', q'<"+str(random)+">', q'<"+str(random2)+">')")
            except:
                if("JP:\xa0Worker Bee" in row[4]):
                    cursor.execute("INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) values (q'<"+row[1]+">', q'<"+row[2]+">', q'<"+row[3]+">', q''"+row[4]+"'', TO_DATE('"+fecha+"','Month DD YYYY'), q'<"+row[6]+">', q'<"+str(random)+">', q'<"+str(random2)+">')")
                elif("'" in row[1]):
                    if("JP:\xa0Starsign" in row[4]):
                        cursor.execute("INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) values (q''"+row[1]+"'', q'<"+row[2]+">', q'<"+row[3]+">', q''"+row[4]+"'', TO_DATE('"+fecha+"','Month DD YYYY'), q'<"+row[6]+">', q'<"+str(random)+">', q'<"+str(random2)+">')")
                    else:
                        cursor.execute("INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) values (q''"+row[1]+"'', q'<"+row[2]+">', q'<"+row[3]+">', q'<"+row[4]+">', TO_DATE('"+fecha+"','Month DD YYYY'), q'<"+row[6]+">', q'<"+str(random)+">', q'<"+str(random2)+">')")
                else:
                    cursor.execute("INSERT INTO Nintendo (nombre, genero, desarrollador, publicador, fechadeestreno, exclusividad, ventasglobales, rating) values (q''<"+row[1]+">'', q''<"+row[2]+">'', q''<"+row[3]+">'', q''<"+row[4]+">'', TO_DATE('"+fecha+"','Month DD YYYY'), q''<"+row[6]+">'', q''<"+str(random)+">', q'<"+str(random2)+">')")
            connection.commit()
        i+=1


contadorinsert=0
menuflag=True


while(menuflag):

    
    print(colored.cyan("Bienvenido a la Base de datos de Sansanoplay, favor de elegir la opción que desee:\n"))
    print(colored.cyan('1.-')+colored.yellow('Funciones CRUD\n'))
    print(colored.cyan('2.-')+colored.yellow('Los 5 exclusivos más caros\n'))
    print(colored.cyan('3.-')+colored.yellow('Los 3 juegos más vendidos\n'))
    print(colored.cyan('4.-')+colored.yellow('Las 3 desarrolladoras con más ventas locales\n'))
    print(colored.cyan('5.-')+colored.yellow('Juegos con mejor rating según fecha de salida\n'))
    print(colored.cyan('6.-')+colored.yellow('Salir\n'))
    print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\nSeleccione su opción: "))
    eleccion=int(input(""))

    if(eleccion==1):
        print(colored.cyan("Seleccione la función CRUD que desea seleccionar:\n"))
        print(colored.cyan("1.-")+colored.yellow("Crear")+colored.cyan("                    (C)\n"))
        print(colored.cyan("2.-")+colored.yellow("Leer")+colored.cyan("                     (R)\n"))
        print(colored.cyan("3.-")+colored.yellow("Actualizar")+colored.cyan("               (U)\n"))
        print(colored.cyan("4.-")+colored.yellow("Borrar")+colored.cyan("                   (D)\n"))
        print(colored.cyan("5.-")+colored.yellow("Volver\n"))
        print(colored.cyan("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSeleccione su opción: "))
        eleccion2=int(input())
        if(eleccion2==1):
            create(cursor)
        if(eleccion2==2):
            read(cursor)
        if(eleccion2==3):
            update(cursor)
        if(eleccion2==4):
            delete(cursor)
        if(eleccion2==5):
            continue
    elif(eleccion==2):
        cincoexclusivos(cursor)
    elif(eleccion==3):
        masvendidos(cursor)
    elif(eleccion==4):
        desarrolladorasventas(cursor)
    elif(eleccion==5):
        rating(cursor)
    elif(eleccion==6):
        menuflag=False
    else:
        print("Opcion incorrecta\n------------------------------------------------------------------------------------------")
    cursor.commit()



connection.close()

































"""
cursor.execute(CREATE OR REPLACE VIEW tabla
AS SELECT SansanoPlay.id, SansanoPlay.nombre, Nintendo.genero, Nintendo.desarrollador, Nintendo.publicador, Nintendo.fechadeestreno, Nintendo.exclusividad, SansanoPlay.precio, SansanoPlay.stock, SansanoPlay.bodega, SansanoPlay.vendidos, Nintendo.ventasglobales, Nintendo.rating
FROM SansanoPlay, Nintendo
WHERE SansanoPlay.id = Nintendo.id
)
"""
