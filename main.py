from flask import Flask, request, jsonify
from microservice import microservice

app = Flask(__name__)

@app.route('/Microservice/', methods=['GET'])
def microservice_init():
    nit = request.args.get('nit')
    mes = request.args.get('mes')
    anio = request.args.get('anio')
    
    if nit is None and mes is None and anio is None:
        return jsonify({'error': 'Se requieren los tres parámetros: id, mes y año'}), 400
    
    print(nit, mes, anio)
    json_file = microservice.ejecucion(nit, mes, anio)
    return json_file

if __name__=="__main__":
    app.run(debug=True)

