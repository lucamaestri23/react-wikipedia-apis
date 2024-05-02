from src.Model.pilot_model import PilotModel
from src.Service.pilot_service import PilotService
from flask import (Blueprint, request, jsonify)
from src.Model.error_model import ErrorModel
pilot_api = Blueprint('pilot_api', __name__, url_prefix="/api/pilot/")

@pilot_api.route('/', methods=['GET'])
def get_pilots():
    service = PilotService()
    payload = service.get_pilots()

    return payload