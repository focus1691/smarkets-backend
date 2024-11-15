from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from ..models.contract import Contract
from .. import db

contract_blueprint = Blueprint('contracts', __name__)

@contract_blueprint.route('/', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    contracts_list = [
        {"id": contract.id, "name": contract.name, "market_id": contract.market_id}
        for contract in contracts
    ]
    return jsonify(contracts_list), 200


@contract_blueprint.route('/', methods=['POST'])
def create_contract():
    data = request.json
    name = data.get('name')
    market_id = data.get('market_id')

    if not name or not market_id:
        raise BadRequest(description="Both 'name' and 'market_id' are required fields.")

    new_contract = Contract(name=name, market_id=market_id)
    db.session.add(new_contract)
    db.session.commit()

    return jsonify({"message": "Contract created successfully", "contract_id": new_contract.id}), 201


@contract_blueprint.route('/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if not contract:
        return jsonify({"error": "Contract not found"}), 404

    return jsonify({"id": contract.id, "name": contract.name, "market_id": contract.market_id}), 200


@contract_blueprint.route('/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    contract = Contract.query.get(contract_id)
    if not contract:
        return jsonify({"error": "Contract not found"}), 404

    db.session.delete(contract)
    db.session.commit()

    return jsonify({"message": "Contract deleted successfully"}), 200
