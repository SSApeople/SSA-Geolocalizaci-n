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


@Clues_bp.route('Cerca/ByDireccion',methods=['POST'])
def CluesCercanosDireccion():
    params = request.get_json()
    busqueda = params.get('busqueda')
    CluesCerca = Acceso().EjecutaStoredProcedure("sp_ObtenerUnidadesMedicasCercanasDireccion", [str(busqueda)])
    return jsonify(CluesCerca)
    

@Clues_bp.route('ById/<IdUnidad>',methods=['GET'])
def CluesById(IdUnidad):
    Clues = Acceso().EjecutaStoredProcedure("sp_ObtenerUnidadMedica", [int(IdUnidad)])
    return jsonify(Clues)
    
 

