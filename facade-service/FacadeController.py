import requests
import os
from flask import Flask, jsonify, request
import uuid 

class FacadeController:
    def __init__(self, facade_port=8080, logging_port=8082, message_port=8081) -> None:
        self.app = Flask(__name__)
        self.facade_port = facade_port
        self.logging_port = logging_port
        self.message_port = message_port
        self.base_url = "http://localhost:"
        self.app.add_url_rule("/facade_service", "post_message", self.post_message, methods=["POST"])
        self.app.add_url_rule("/facade_service", "get_message", self.get_message, methods=["GET"])

    def post_message(self):
        id = str(uuid.uuid4())
        msg = request.get_json()
        requests.post(f"{self.base_url}{self.logging_port}/log", json={"msg": msg, "id": id})
        return "", 200

    def get_message(self):
        response_log = requests.get(f"{self.base_url}{self.logging_port}/log")
        response_mes = requests.get(f"{self.base_url}{self.message_port}/message")
        return jsonify(response_log.json(), response_mes.json())

    def run(self, debug=False):
        self.app.run(port=self.facade_port, debug=debug)

if __name__ == "__main__":
    app = FacadeController()
    app.run(debug=True)
