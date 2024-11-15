from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from . import db
from .models import Event, Market, Contract

# Create a Blueprint for routes
api_blueprint = Blueprint('api', __name__)


# Create a Contract
@api_blueprint.route('/api/contracts', methods=['POST'])
def create_contract():
    data = request.json
    name = data.get('name')
    market_id = data.get('market_id')

    new_contract = Contract(name=name, market_id=market_id)
    db.session.add(new_contract)
    db.session.commit()

    return jsonify({"message": "Contract created successfully", "contract_id": new_contract.id}), 201



# Get all Contracts
@api_blueprint.route('/api/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    contracts_list = [
        {"id": contract.id, "name": contract.name, "market_id": contract.market_id}
        for contract in contracts
    ]
    return jsonify(contracts_list), 200


# Get a single Market by ID
@api_blueprint.route('/api/markets/<int:market_id>', methods=['GET'])
def get_market(market_id):
    market = Market.query.get(market_id)
    if not market:
        return jsonify({"error": "Market not found"}), 404

    return jsonify({"id": market.id, "name": market.name, "event_id": market.event_id}), 200

# Get a single Contract by ID
@api_blueprint.route('/api/contracts/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if not contract:
        return jsonify({"error": "Contract not found"}), 404

    return jsonify({"id": contract.id, "name": contract.name, "market_id": contract.market_id}), 200



# Delete a Contract
@api_blueprint.route('/api/contracts/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if not contract:
        return jsonify({"error": "Contract not found"}), 404

    db.session.delete(contract)
    db.session.commit()

    return jsonify({"message": "Contract deleted successfully"}), 200
