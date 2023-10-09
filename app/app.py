from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

@app.route('/', methods=['GET'])
def homepage():
    return 'Superheroes API....SUPERHEROES ASSEMBLE!'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]
    return jsonify(hero_list)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_powers = [{"id": hero_power.power.id, "name": hero_power.power.name, "description": hero_power.power.description} for hero_power in hero.hero_powers]

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": hero_powers
    }

    return jsonify(hero_data)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_list = [{"id": power.id, "name": power.name, "description": power.description} for power in powers]
    return jsonify(power_list)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(power_data)

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    new_description = data.get("description")

    if not new_description or len(new_description) < 20:
        return jsonify({"errors": ["Validation error: Description must be present and at least 20 characters long"]}), 400

    power.description = new_description
    db.session.commit()

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength")

    if not hero_id or not power_id or not strength:
        return jsonify({"errors": ["Validation error: Missing required fields"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["Validation error: Hero or Power not found"]}), 400

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Validation error: Choose Strength- 'Strong', 'Weak', 'Average'"]}), 400

    hero_power = HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    hero_powers = [{"id": hero_power.power.id, "name": hero_power.power.name, "description": hero_power.power.description} for hero_power in hero.hero_powers]

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": hero_powers
    }

    return jsonify(hero_data), 201

if __name__ == '__main__':
    app.run(port=5555)
