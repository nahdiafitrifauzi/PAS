from . import db
from datetime import datetime

class Materi(db.Model):
    __tablename__ = 'materi'  
    __table_args__ = {'extend_existing': True}  
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False, unique=True)  
    isi = db.Column(db.Text, nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
