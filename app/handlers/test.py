import logging

from flask_restful import Resource
from flask import request

logger = logging.getLogger(__name__)

class Hello(Resource):
	"""docstring for Hello"""
	def get(self):
		return "Hello"
