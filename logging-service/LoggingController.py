import requests
import os
from flask import Flask, jsonify, request

class LoggingController:
    def __init__(self, facade_port=8080, logging_port=8082, message_port=8081) -> None:
        self.app = Flask(__name__)
        self.facade_port = facade_port
        self.logging_port = logging_port
        self.message_port = message_port
        self.base_url = "http://localhost:"
        self.messages = {}
        self.app.add_url_rule("/log", "post_log", self.post_log, methods=["POST"])
        self.app.add_url_rule("/log", "get_log", self.get_log, methods=["GET"])

    def post_log(self):
        msg, id = request.json.get("msg"), request.json.get("id")
        self.messages[id] = msg
        print(f"logged: id:{id}, msg:{msg}")
        return "", 200

    def get_log(self):
        return jsonify(list(self.messages.values()))
    
    def run(self, debug=False):
        self.app.run(port=self.logging_port, debug=debug)

if __name__ == "__main__":
    app = LoggingController()
    app.run(debug=True)
