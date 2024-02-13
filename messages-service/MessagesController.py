import requests
import os
from flask import Flask, jsonify, request

class MessagesController:
    def __init__(self, facade_port=8080, logging_port=8082, message_port=8081) -> None:
        self.app = Flask(__name__)
        self.facade_port = facade_port
        self.logging_port = logging_port
        self.message_port = message_port
        self.base_url = "http://localhost:"
        self.app.add_url_rule("/message", "get_message", self.get_message, methods=["GET"])

    def get_message(self):
        return jsonify("message service is not implemented yet")
        
    def run(self, debug=False):
        self.app.run(port=self.message_port, debug=debug)

if __name__ == "__main__":
    app = MessagesController()
    app.run(debug=True)
