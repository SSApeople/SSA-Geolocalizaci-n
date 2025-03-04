from flask import Flask, jsonify, request
from utils.db import Acceso
from flask import Blueprint
from flask_jwt_extended import jwt_required
from decouple import config
from utils.CallOpenAI import OpenAIConector

Localidades_bp = Blueprint('Ub', __name__)

@Localidades_bp.route('Estados',methods=['GET'])
def GetEstados():
    Estados = Acceso().EjecutaStoredProcedure("SP_ObtenerUbicaciones", ["ENTIDAD",None,None,None])
    return jsonify(Estados)
    
@Localidades_bp.route('Estados/Municipios/<Mun>',methods=['GET'])
def GetMunicipios(Mun):
    Estados = Acceso().EjecutaStoredProcedure("SP_ObtenerUbicaciones", ["MUNICIPIO",int(Mun),None,None])
    return jsonify(Estados)

@Localidades_bp.route('Estados/Municipios/<Mun>/Localidad/<Local>',methods=['GET'])
def GetLocalidades(Mun,Local):
    Estados = Acceso().EjecutaStoredProcedure("SP_ObtenerUbicaciones", ["LOCALIDAD",int(Mun),int(Local),None])
    return jsonify(Estados)


@Localidades_bp.route('Localidad/<Localidad>',methods=['GET'])
def GetLocalidadesEstMun(Localidad):
    Estados = Acceso().EjecutaStoredProcedure("SP_ObtenerUbicaciones", ["LOC_MUN_ESTA",None, None, Localidad])
    return jsonify(Estados)