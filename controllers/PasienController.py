from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Perawats, db, PerawatsSchema, Pasiens, PasiensSchema, Dokters, DoktersSchema
from marshmallow import validate

pasiens_schema = PasiensSchema()
pasien_schema = PasiensSchema(many=True)

#CRUD Pasien
def index():
    pasien = Pasiens.query.all()
    response = []
    for pasiens in pasien: response.append(pasiens.to_dict())
    return jsonify(response), 200

def store():
    try:
        request_form = request.form.to_dict()
        errors = pasiens_schema.validate(request_form, session=db.session)
        if(errors):
            return jsonify({"Error: ": errors}), 400
        new_pasiens = Pasiens(
            nama = request_form['nama'],
            alamat = request_form['alamat'],
            diagnosa = request_form['diagnosa']
        )
  
        db.session.add(new_pasiens)
        db.session.commit()
  
        return jsonify({"message": "Data berhasil ditambahkan"}), 201
 
    except Exception as e:
     
        return jsonify({'error': str(e)}), 500

def show(id_pasien):
    response = Pasiens.query.get(id_pasien)
    if(response):
        response = Pasiens.query.get(id_pasien).to_dict()
        return jsonify(response)
    else:
        return jsonify({"message": "Data not found"}), 404

def update(id_pasien):
    data = Pasiens.query.get(id_pasien)
    if(data):
        request_form = request.form.to_dict()
        data.nama = request_form['nama']
        data.alamat = request_form['alamat']
        data.diagnosa = request_form['diagnosa']
        db.session.commit()
        return jsonify({"data": "Data berhasil diupdate"}), 200
    else:
        return jsonify({"message": "Data tidak ditemukan"}), 404

def delete(id_pasien):
    check = Pasiens.query.get(id_pasien)
    if(check):
        Pasiens.query.filter_by(id_pasien = id_pasien).delete()
        db.session.commit()
        return jsonify({"message": "Data berhasil dihapus"}), 200
    else:
        return jsonify({"message": "Data not found", "status": 400})
    