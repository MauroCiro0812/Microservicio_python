from flask import Flask
from microservice import microservice

app = Flask(__name__)

@app.route('/Microservice')
def microservice_init():
    microservice.ejecucion()
    return "ejecuto"

if __name__=="__main__":
    app.run(debug=True)

