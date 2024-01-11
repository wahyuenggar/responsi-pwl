from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Perawats, db, PerawatsSchema, Pasiens, PasiensSchema, Dokters, DoktersSchema
from marshmallow import validate

dokters_schema = DoktersSchema()
dokter_schema = DoktersSchema(many=True)

#CRUD Dokter
def index():
    dokter = Dokters.query.all()
    response = []
    for dokters in dokter: response.append(dokters.to_dict())
    return jsonify(response), 200

def store():
    try:
        request_form = request.form.to_dict()
        errors = dokters_schema.validate(request_form, session=db.session)
        if(errors):
            return jsonify({"Error: ": errors}), 400
        new_dokters = Dokters(
            nama_dokter = request_form['nama_dokter'],
            alamat = request_form['alamat'],
            spesialis = request_form['spesialis']
        )
  
        db.session.add(new_dokters)
        db.session.commit()
  
        return jsonify({"message": "Data berhasil ditambahkan"}), 201
 
    except Exception as e:
     
        return jsonify({'error': str(e)}), 500

def show(npm_dokter):
    response = Dokters.query.get(npm_dokter)
    if(response):
        response = Dokters.query.get(npm_dokter).to_dict()
        return jsonify(response)
    else:
        return jsonify({"message": "Data not found"}), 404

def update(npm_dokter):
    data = Dokters.query.get(npm_dokter)
    if(data):
        request_form = request.form.to_dict()
        data.nama_dokter = request_form['nama_dokter']
        data.alamat = request_form['alamat']
        data.spesialis = request_form['spesialis']
        db.session.commit()
        return jsonify({"data": "Data berhasil diupdate"}), 200
    else:
        return jsonify({"message": "Data tidak ditemukan"}), 404

def delete(npm_dokter):
    check = Dokters.query.get(npm_dokter)
    if(check):
        Dokters.query.filter_by(npm_dokter = npm_dokter).delete()
        db.session.commit()
        return jsonify({"message": "Data berhasil dihapus"}), 200
    else:
        return jsonify({"message": "Data not found", "status": 400})