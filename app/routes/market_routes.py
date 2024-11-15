from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from ..models.market import Market
from .. import db

market_blueprint = Blueprint('market', __name__)

@market_blueprint.route('/', methods=['GET'])
def get_markets():
    markets = Market.query.all()
    markets_list = [
        {"id": market.id, "name": market.name, "event_id": market.event_id}
        for market in markets
    ]
    return jsonify(markets_list), 200


@market_blueprint.route('/', methods=['POST'])
def create_market():
    data = request.json
    name = data.get('name')
    event_id = data.get('event_id')

    if not name or not event_id:
        raise BadRequest(description="Both 'name' and 'event_id' are required fields.")

    new_market = Market(name=name, event_id=event_id)
    db.session.add(new_market)
    db.session.commit()

    return jsonify({"message": "Market created successfully", "market_id": new_market.id}), 201


@market_blueprint.route('/<int:market_id>', methods=['DELETE'])
def delete_market(market_id):
    market = Market.query.get(market_id)
    if not market:
        return jsonify({"error": "Market not found"}), 404

    db.session.delete(market)
    db.session.commit()

    return jsonify({"message": "Market deleted successfully"}), 200