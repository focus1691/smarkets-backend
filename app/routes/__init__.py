from flask import Blueprint

from .event_routes import event_blueprint
from .market_routes import market_blueprint
from .contract_routes import contract_blueprint

api_blueprint = Blueprint('api', __name__)

api_blueprint.register_blueprint(event_blueprint, url_prefix='/events')
api_blueprint.register_blueprint(market_blueprint, url_prefix='/markets')
api_blueprint.register_blueprint(contract_blueprint, url_prefix='/contracts')
