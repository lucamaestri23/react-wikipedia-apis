import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS  # Importa Flask-CORS

from src.Controller.pilot_controller import pilot_api

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le rotte
app.url_map.strict_slashes = False
app.register_blueprint(pilot_api)



@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {
            "id": 1,
            "name": "Max Verstappen",
            "team": "Oracle Red Bull Racing",
            "gpWin": 58,
            "gpMade": 190,
            "podiums": 102,
            "points": 2695.5,
            "pole": 37,
            "fastLaps": 32
        },
         {
            "id": 1,
            "name": "Charles Leclerc",
            "team": "Scuderia Ferrari HP",
            "gpWin": 5,
            "gpMade": 130,
            "podiums": 32,
            "points": 1150,
            "pole": 23,
            "fastLaps": 9
        }
    ]
    return jsonify(data)

logfile = os.path.join(os.path.dirname(__file__), "app.log")
logging.basicConfig(filename=logfile, level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True)
