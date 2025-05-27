from flask import Blueprint, render_template, request, redirect, url_for
from .models import Materi
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/materi')
def materi_list():
    materi = Materi.query.all()
    return render_template('materi_list.html', materi=materi)

@main.route('/materi/tambah', methods=['GET', 'POST'])
def tambah_materi():
    if request.method == 'POST':
        judul = request.form['judul']
        isi = request.form['isi']
        new_materi = Materi(judul=judul, isi=isi)
        db.session.add(new_materi)
        db.session.commit()
        return redirect(url_for('main.materi_list'))
    return render_template('materi_form.html')

@main.route('/kuis')
def kuis():
    return render_template('kuis.html')
