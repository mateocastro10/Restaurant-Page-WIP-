import sqlalchemy
from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__='Usuario'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    correo=db.Column(db.String(120), unique=True, nullable=False)
    clave=db.Column(db.String(120), nullable=False)
    recetas=db.relationship('Receta', backref='Usuario', cascade="all, delete-orphan")

class Receta(db.Model):
    __tablename__='Receta'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    tiempo=db.Column(db.Integer, nullable=False)
    fecha=db.Column(db.DateTime, nullable=False)
    elaboracion=db.Column(db.String(80), nullable=False)
    cantidadmegusta=db.Column(db.Integer, nullable=False)
    usuarioid=db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    ingredientes=db.relationship('Ingrediente', backref='Receta', cascade="all, delete-orphan")


class Ingrediente(db.Model):
    __tablename__='Ingrediente'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    cantidad=db.Column(db.Integer, nullable=False)
    unidad=db.Column(db.String(80), nullable=False)
    recetaid=db.Column(db.Integer, db.ForeignKey('Receta.id'))
