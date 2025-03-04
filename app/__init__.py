from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)



def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para todas las rutas
    
    app.config["JWT_SECRET_KEY"] = "PMS2024_PEOPL3M3D14"
    jwt = JWTManager(app)
    # Importar y registrar Blueprints
    from .auth import auth_bp
    from CluesCercanos import Clues_bp
    from Localidades import Localidades_bp
 
    
     
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(Clues_bp, url_prefix="/Clues")
    app.register_blueprint(Localidades_bp, url_prefix="/Localidades")
    
    
 
    
    
    return app