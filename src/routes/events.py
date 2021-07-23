from flask import Blueprint

events_routes = Blueprint("events_routes", __name__)

@events_routes.route("/events", methods=["GET"])
def get_events():
	pass