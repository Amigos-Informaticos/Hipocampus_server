from flask import Flask
from flask_cors import CORS

from src.routes.events import events_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(events_routes)


@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=42080, ssl_context=("cert.pem", "key.pem"))
