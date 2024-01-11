from flask import Flask
from flask_migrate import Migrate
from models.modelTables import db
from routes.perawats_bp import perawats_bp
from routes.pasiens_bp import pasiens_bp
from routes.dokters_bp import dokters_bp 

app = Flask(__name__)

@app.route("/")
def start():
    return """
    Masuk Ke /perawat
    Masuk ke /dokter
    Masuk ke /pasiien"""

app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(perawats_bp, url_prefix='/perawat')
app.register_blueprint(pasiens_bp, url_prefix='/pasien')
app.register_blueprint(dokters_bp, url_prefix='/dokter')

if __name__ == '__main__':                  
    app.run(port=8000, debug=True)
