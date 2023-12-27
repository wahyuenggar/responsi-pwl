from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
 
db = SQLAlchemy()
 
class Perawats(db.Model):
 
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
    
 
class PerawatsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Perawats
        load_instance = True
  
        
    nama = fields.String(required = True, validate = validate.Length(min=1, error="nama tidak boleh kosong"))
    alamat = fields.String(required = True, validate = validate.Length(min=1, error="alamat tidak boleh kosong"))
    jabatan = fields.String(required = True, validate = validate.Length(min=1, error="jabatan tidak boleh kosong"))