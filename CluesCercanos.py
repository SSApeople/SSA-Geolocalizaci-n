from flask import Flask, jsonify, request
from utils.db import Acceso
from flask import Blueprint
from flask_jwt_extended import jwt_required
from utils.CallOpenAI import OpenAIConector


Clues_bp = Blueprint('Clues', __name__)

@Clues_bp.route('Cerca/<latitud>/<longuitud>/<distancia>',methods=['GET'])
def CluesCercanos(latitud,longuitud,distancia):
    CluesCerca = Acceso().EjecutaStoredProcedure("sp_ObtenerUnidadesMedicasCercanas", [float(latitud),float(longuitud),int(distancia)])
    return jsonify(CluesCerca)
    
    

