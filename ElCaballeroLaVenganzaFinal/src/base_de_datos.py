import sqlite3

# Insert into tabla([lista_campos]) values ([lista_valores])
# SELECT *
# FROM EMPLEADOS
# WHERE puntuacion > 1000
# Order by asc | desc
# limit 2

# sentencia = ''' select * from Jugadores ''' order by puntuacion desc limit 3

with sqlite3.connect("base_de_datos.db") as conexion:
    try:
        #CREATE TABLE
        sentencia = '''
                    create table Jugadores
                    (
                        id integer primary key autoincrement,
                        nombre text,
                        puntuacion integer,
                        nivel text
                    )
                    '''
#         sentencia = '''
#         alter table Empleados add balas real
#         '''        
        conexion.execute(sentencia)
        print("Tabla creada con exito")
    except:
        print("Error!!!")

# with sqlite3.connect("base_de_datos.db") as conexion:
#     try:
#         nombre = "Ivan"
#         puntuacion = 1000
#         sentencia = '''
#                     insert into Jugadores (nombre, puntuacion) values (?, ?)
#                     '''
#         conexion.execute(sentencia, (nombre, puntuacion))
#         print("Dato insertado con exito")
#     except:
#         print("Error!!!")