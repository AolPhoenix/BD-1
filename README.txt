Sebastian Campos 201773517-1
Matias Silva 201773531-7

Uso de la tarea:
Para poder utilizar la tarea correctamente se deben tener instaladas las siguientes librerias:
-pyodbc
-csv
-random
-clint
-os
-msvcrt
-time
La mayoria de las libreroas deberian venir instaladas por defecto excepto,por ejemplo, clint (para lo �nico que se uso esta libreria fue para colorear el texto) o pyodbc (
 m�todo de conexi�n python-base de datos), en caso de no tenerla instalarla por la via normal (pip install clint en la consola). Favor de corroborar que todas las librer�as
est�n instaladas antes de correr el programa.
Se utilizo oracle 11g para la realizacion de la tarea.
Al iniciar el programa, se le pedir�n 4 datos respecto a su base de datos, los cuales son:
DSN=Driver de su base de datos para conexiones externas,se debe escribir su nombre exactamente. El driver de oracle 11g permite colocar nombres personalizados, deberia 
funcionar de todas maneras.
DBQ=Nombre de su base de datos
Uid= Nombre de usuario para acceder a su base de datos (por defecto es SYSTEM)
Pwd= Contrase�a para el acceso de su base de datos.
Cuidado con la escritura, cualquier error en la introducci�n de estos 4 datos puede causar fallas.