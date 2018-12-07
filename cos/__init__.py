from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./frontend/dist/static",
            static_url_path = "/clients/onlineorderbackend/static",
            template_folder = "./frontend/dist")
CORS(app, origins=['http://localhost:20000',
                  'http://www.cdmorales.net',
                   'http://localhost:5000',
                   'http://127.0.0.1:5000'])

@app.route('/clients/onlineorderbackend')
def index():
    return render_template('index.html')

@app.route('/clients/onlineorderbackend/api/getmenu', methods=['GET'])
def get_menu():
    menu = [
            {
                'id': 0,
                'name': 'taco'
            },
            {
                'id': 1,
                'name': 'burrito'
            },
            {
                'id': 2,
                'name': 'margarita'
            },
            {
                'id': 3,
                'name': 'chimichanga'
            },
            {
                'id': 4,
                'name': 'al pastor'
            },
            {
                'id': 5,
                'name': 'cochinita pibil'
            }
    ]
    response = jsonify(menu)
    return response
