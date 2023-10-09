from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)
    hero_powers = db.relationship('HeroPower', back_populates='hero')

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name must be present")
        return value

    @validates('super_name')
    def validate_super_name(self, key, value):
        if not value:
            raise ValueError("Super Name must be present")
        return value

class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    power_heroes = db.relationship('HeroPower', back_populates='power')

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name must be present")
        return value

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be present and at least 20 characters long")
        return value

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='power_heroes')

    @validates('strength')
    def validate_strength(self, key, value):
        allowed_strengths = ['Strong', 'Weak', 'Average']
        if value not in allowed_strengths:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        return value
