from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Perawats, db, PerawatsSchema
from marshmallow import validate
 
perawats_schema = PerawatsSchema()
perawat_schema = PerawatsSchema(many=True)
 
def index():
    perawat = Perawats.query.all()
    response = []
    for perawats in perawat: response.append(perawats.to_dict())
    return jsonify(response), 200

def store():
    
    try:
        request_form = request.form.to_dict()
        errors = perawats_schema.validate(request_form, session=db.session)
        if(errors):
            return jsonify({"Error: ": errors}), 400
        new_perawats = Perawats(
            nama = request_form['nama'],
            alamat = request_form['alamat'],
            jabatan = request_form['jabatan']
        )
  
        db.session.add(new_perawats)
        db.session.commit()
  
        return jsonify({"message": "Data berhasil ditambahkan"}), 201
 
    except Exception as e:
     
        return jsonify({'error': str(e)}), 500

def show(npm_perawat):
    response = Perawats.query.get(npm_perawat)
    if(response):
        response = Perawats.query.get(npm_perawat).to_dict()
        return jsonify(response)
    else:
        return jsonify({"message": "Data not found"}), 404

def update(npm_perawat):
    data = Perawats.query.get(npm_perawat)
    if(data):
        request_form = request.form.to_dict()
        data.nama = request_form['nama']
        data.alamat = request_form['alamat']
        data.jabatan = request_form['jabatan']
        return jsonify({"data": "Data berhasil diupdate"}), 200
    else:
        return jsonify({"message": "Data tidak ditemukan"}), 404

def delete(npm_perawat):
    check = Perawats.query.get(npm_perawat)
    if(check):
        Perawats.query.filter_by(npm_perawat=npm_perawat).delete()
        db.session.commit()
        return jsonify({"message": "Data berhasil dihapus"}), 200
    else:
        return jsonify({"message": "Data not found", "status": 400})