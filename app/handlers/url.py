import logging
import datetime
import random
import string

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DataError
from marshmallow import ValidationError

from flask_restful import Resource
from flask import request, jsonify, abort, redirect

from app.models.url_model import Url, UrlSchema
from app.models import *
from app import flask_app

logger = logging.getLogger(__name__)

class Urlapi(Resource):
	"""docstring for Urlapi"""
	def post(self):
		try:
			request_data = request.get_json()
			token = self.randomString()
			request_data['token'] = token
			dataSchema = UrlSchema().load(request_data).data
			db.session.add(dataSchema)
			db.session.commit()
			db.session.close()
			response = {}
			response['short-url'] = request.url_root + 's/' + token
			return jsonify(data=response, status=200)
		except DataError as e:
			logger.exception(str(e))
			return jsonify(status=400, msg="Data error")
		except NoResultFound as e:
			logger.exception(str(e))
			return jsonify(status=400, msg=str(e))
		except Exception as e:
			logger.exception(str(e))
			return jsonify(status=400, msg=str(e))

	def randomString(self, stringlength=10):
		"""Generate a random string of fixed length """
		letters = string.ascii_lowercase
		return ''.join(random.sample(letters,stringlength))


@flask_app.route('/s/<token>')
def token(token):
	try:
		current = datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')
		query = Url.query.filter(Url.token==token, Url.expire_date >= current).all()
		data = UrlSchema(many=True).dump(query).data
		if not data:
			abort(404)
		url_redirect = data[0]['url']
		if not url_redirect.startswith("http://"):
			url_redirect = "http://" + url_redirect
		return redirect(url_redirect, code=302)
	except Exception as e:
		return jsonify(msg=str(e), status=400)