# app/__init__.py
import os
import logging
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')
    
    # Pastikan folder logs ada
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Setup logging untuk error log
    logging.basicConfig(
        filename='logs/error.log',
        level=logging.ERROR,
        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    
    # Registrasi blueprint (route)
    from app import routes
    app.register_blueprint(routes.main_bp)
    
    return app
