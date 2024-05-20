import psycopg2

'''
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'root',
        database = 'prueba',
        port = '5432'
    )
    print("Conexion Exitosa")
except Exception as ex:
    print(ex)

cur = connection.cursor()

cur.execute("SELECT nombre, apellidos FROM empleados")

for nombre, apellidos in cur.fetchall():
    print(nombre, apellidos)

connection.close()
'''

class postgres():
    def conexion_db():
        try:
            connection = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = 'root',
                database = 'prueba',
                port = '5432'
            )
            print("Conexion Exitosa")
        except Exception as ex:
            print(ex)
        
        
        cur = connection.cursor()

        cur.execute("SELECT nombre, apellidos FROM empleados")

        for nombre, apellidos in cur.fetchall():
            print(nombre, apellidos)

        
        connection.close()

'''   def query_db(self):
        cur = self.connection.cursor()

        cur.execute("SELECT nombre, apellidos FROM empleados")

        for nombre, apellidos in cur.fetchall():
            print(nombre, apellidos)

    def cerrar_db(self):
        self.connection.close()'''