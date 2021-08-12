import json

from flask import Blueprint, Response, request
from pymongo import MongoClient

from src.configuration.JSONhandler import JSONHandler
from src.configuration.paths import api_configuration_path
from src.routes.HTTPStatus import BAD_REQUEST, NOT_FOUND, NO_CONTENT, OK

connection = MongoClient(JSONHandler.load("connection_string", False, api_configuration_path))
collection = connection["hipocampus"]["events"]

events_routes = Blueprint("events_routes", __name__)


@events_routes.route("/events", methods=["GET"])
def get_events():
	fechas: list = collection.find_one({})["fechas"]
	response = Response(status=NO_CONTENT)
	if fechas:
		response = Response(
			json.dumps(fechas),
			status=OK,
			mimetype="application/json"
		)
	return response


@events_routes.route("/events", methods=["POST"])
def save_event():
	json_values = request.json
	response = Response(status=BAD_REQUEST)
	if "fecha" in json_values:
		fechas: list = collection.find_one({})["fechas"]
		fechas.append(json_values["fecha"])
		collection.update_one({"name": "edson"}, {"$set": {"fechas": fechas}})
		response = Response(status=OK)
	return response


@events_routes.route("/events", methods=["DELETE"])
def delete_event():
	json_values = request.json
	response = Response(status=BAD_REQUEST)
	if "fecha" in json_values:
		fechas: list = collection.find_one({})["fechas"]
		response = Response(status=NOT_FOUND)
		if json_values["fecha"] in fechas:
			fechas.remove(json_values["fecha"])
			response = Response(status=OK)
	return response
