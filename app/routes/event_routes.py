from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from ..models.event import Event
from .. import db

event_blueprint = Blueprint('events', __name__)

@event_blueprint.route('/', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = [
        {
            "id": event.id,
            "name": event.name,
            "start_time": event.start_time,
            "type": event.type,
            "markets": [
                {
                    "id": market.id,
                    "name": market.name,
                    "event_id": market.event_id,
                    "contracts": [
                        {
                            "id": contract.id,
                            "name": contract.name,
                            "market_id": contract.market_id,
                        }
                        for contract in market.contracts
                    ],
                }
                for market in event.markets
            ],
        }
        for event in events
    ]
    return jsonify(events_list), 200


@event_blueprint.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    event_data = {
        "id": event.id,
        "name": event.name,
        "start_time": event.start_time,
        "type": event.type,
        "markets": [
            {
                "id": market.id,
                "name": market.name,
                "event_id": market.event_id,
                "contracts": [
                    {
                        "id": contract.id,
                        "name": contract.name,
                        "market_id": contract.market_id,
                    }
                    for contract in market.contracts
                ],
            }
            for market in event.markets
        ],
    }
    return jsonify(event_data), 200


@event_blueprint.route('/', methods=['POST'])
def create_event():
    data = request.json

    if not data:
        raise BadRequest(description="Request body is missing or invalid.")

    required_fields = ['name', 'start_time', 'type']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(description=f"Missing required fields: {', '.join(missing_fields)}")

    name = data.get('name')
    start_time = data.get('start_time')
    type = data.get('type')

    new_event = Event(name=name, start_time=start_time, type=type)
    db.session.add(new_event)
    db.session.commit()

    return jsonify({"message": "Event created successfully", "event_id": new_event.id}), 201


@event_blueprint.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "Event deleted successfully"}), 200