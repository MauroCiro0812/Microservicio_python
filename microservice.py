from post import postgres

class microservice(postgres):

    def ejecucion():
        postgres.conexion_db()
        #postgres.query_db()
        #postgres.cerrar_db