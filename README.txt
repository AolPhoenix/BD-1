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
La mayoria de las libreroas deberoan venir instaladas por defecto excepto por clint (para lo único que se uso esta libreria fue para colorear el texto), en caso de no tenerla
instalarla por la via normal (pip install clint en la consola).
Se utilizo oracle 11g para la realizacion de la tarea.
Al iniciar el programa, se le pedirán 4 datos respecto a su base de datos, los cuales son:
DSN=Driver de su base de datos para conexiones externas,se debe escribir su nombre exactamente. El driver de oracle 11g permite colocar nombres personalizados, deberia 
funcionar de todas maneras.
DBQ=Nombre de su base de datos
Uid= Nombre de usuario para acceder a su base de datos (por defecto es SYSTEM)
Pwd= Contraseña para el acceso de su base de datos.
Cuidado con la escritura, cualquier error en la introducción de estos 4 datos puede causar fallas.