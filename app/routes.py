from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, this is a Flask API with SQLAlchemy!"})
