from flask import Flask
from flask_migrate import Migrate
from models.modelTables import db
from routes.perawats_bp import perawats_bp

app = Flask(__name__)

@app.route("/")
def start():
    return "Masuk Ke /perawat"

app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(perawats_bp, url_prefix='/perawat')

if __name__ == '__main__':
    app.run(port=8000, debug=True)