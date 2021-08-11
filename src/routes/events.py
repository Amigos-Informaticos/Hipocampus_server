import json

from flask import Blueprint, Response
from pymongo import MongoClient

from src.configuration.JSONhandler import JSONHandler
from src.configuration.paths import api_configuration_path

connection = MongoClient(JSONHandler.load("connection_string", False, api_configuration_path))
collection = connection["hipocampus"]["events"]

events_routes = Blueprint("events_routes", __name__)


@events_routes.route("/events", methods=["GET"])
def get_events():
	response = Response(status=204)
	fechas: list = collection.find_one({})["fechas"]
	response = Response(
		json.dumps(fechas),
		status=200,
		mimetype="application/json"
	)
	return response
