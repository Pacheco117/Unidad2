import sqlite3

# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("base_prueba.db")
# Creamos (si no existe) una tabla creada alumnos con sus campos
conexion.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    apellido varchar,
                    edad integer,
                    genero varchar,
                    domicilio varchar
                    )""")
conexion.close()
conexion = sqlite3.connect("base_prueba.db")
# Insertamos dos alumnos
conexion.execute("Insert into alumnos(nombre,apellido,edad,genero,domicilio) values(?,?,?,?,?)", ("Nayelly", "Basto", 27, "Femenino", "Chicxulub"))
# Este es necesario para que se ejecuten las consultas anteriores
conexion.commit()

# Recuperamos un elementos de la tabla alumnos y lo imprimimos
alumno = conexion.execute("select * from alumnos where nombre = 'Nayelly'")
# Traemos todo
fila = alumno.fetchone()
#imprimimos la fila (el alumno)
print(fila)
# Cerramos la conexión con SQLITE
conexion.close()
