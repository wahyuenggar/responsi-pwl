from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
 
db = SQLAlchemy()
 
class Perawats(db.Model): #buat duplicate 3
 
    __tablename__ = 'perawat'
 
    npm_perawat = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    jabatan = db.Column(db.String(200), nullable=False)
 
    def to_dict(self):
        return {
            'npm_perawat': self.npm_perawat,
            'nama': self.nama,
            'alamat': self.alamat,
            'jabatan': self.jabatan,
        }
    
class Pasiens(db.Model): #buat duplicate 3
 
    __tablename__ = 'pasien'
 
    id_pasien = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    diagnosa = db.Column(db.String(200), nullable=False)
 
    def to_dict(self):
        return {
            'id_pasien': self.id_pasien,
            'nama': self.nama,
            'alamat': self.alamat,
            'diagnosa': self.diagnosa,
        }
    
class Dokters(db.Model): #buat duplicate 3
 
    __tablename__ = 'dokter'
 
    npm_dokter = db.Column(db.Integer, primary_key=True)
    nama_dokter = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    spesialis = db.Column(db.String(200), nullable=False)
 
    def to_dict(self):
        return {
            'npm_dokter': self.npm_dokter,
            'nama_dokter': self.nama_dokter,
            'alamat': self.alamat,
            'spesialis': self.spesialis,
        }
    
 
class PerawatsSchema(SQLAlchemyAutoSchema): #buat duplicate 3
    class Meta:
        model = Perawats
        load_instance = True
  
        
    nama = fields.String(required = True, validate = validate.Length(min=1, error="nama tidak boleh kosong"))
    alamat = fields.String(required = True, validate = validate.Length(min=1, error="alamat tidak boleh kosong"))
    jabatan = fields.String(required = True, validate = validate.Length(min=1, error="jabatan tidak boleh kosong"))


class PasiensSchema(SQLAlchemyAutoSchema): #buat duplicate 3
    class Meta_1:
        model = Pasiens
        load_instance = True
  
        
    nama = fields.String(required = True, validate = validate.Length(min=1, error="nama tidak boleh kosong"))
    alamat = fields.String(required = True, validate = validate.Length(min=1, error="alamat tidak boleh kosong"))
    diagnosa = fields.String(required = True, validate = validate.Length(min=1, error="diagnosa tidak boleh kosong"))

class DoktersSchema(SQLAlchemyAutoSchema): #buat duplicate 3
    class Meta_2:
        model = Dokters
        load_instance = True
  
        
    nama_dokter = fields.String(required = True, validate = validate.Length(min=1, error="nama tidak boleh kosong"))
    alamat = fields.String(required = True, validate = validate.Length(min=1, error="alamat tidak boleh kosong"))
    spesialis = fields.String(required = True, validate = validate.Length(min=1, error="jabatan tidak boleh kosong"))