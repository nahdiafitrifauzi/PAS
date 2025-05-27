from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


class Materi(db.Model):
    __tablename__ = 'materi'
    
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(255), nullable=False)
    isi = db.Column(db.Text, nullable=False)


def tambah_materi_awal():
    if Materi.query.count() == 0:
        materi_list = [
            {"judul": "Konsep Dasar Ilmu Ekonomi", "isi": "Sejak ditulis dan diterbitkannya buku berjudul 'The Wealth of Nations' pada tahun 1776 oleh Adam Smith, ilmu ekonomi mengalami perkembangan pesat..."},
            {"judul": "Sistem Perekonomian", "isi": "Ada berbagai sistem ekonomi seperti kapitalisme, sosialisme, dan campuran..."},
            {"judul": "Pelaku Ekonomi", "isi": "Pelaku ekonomi adalah cara suatu negara mengelola sumber daya dan distribusi barang/jasa..."},
            {"judul": "Masalah Ekonomi", "isi": "Masalah utama dalam ekonomi meliputi kelangkaan, inflasi, pengangguran, dan kemiskinan..."},
            {"judul": "Teori Ekonomi Mikro dan Makro", "isi": "Ekonomi Mikro fokus pada individu dan perusahaan, sedangkan Ekonomi Makro fokus pada skala nasional..."}
        ]

        try:
            for data in materi_list:
                new_materi = Materi(judul=data["judul"], isi=data["isi"])
                db.session.add(new_materi)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error saat menambahkan data: {e}")  


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekonomi.db'

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    with app.app_context():
       
        db_path = "ekonomi.db"
        if not os.path.exists(db_path):
            open(db_path, 'w').close()
            print("✅ File ekonomi.db berhasil dibuat!")

        db.create_all()  
        tambah_materi_awal()  
    return app
