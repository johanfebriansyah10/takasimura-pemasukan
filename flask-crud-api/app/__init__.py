from flask import Flask
from flask_cors import CORS


def createApp():
  app = Flask(__name__)
  CORS(app)
  return app