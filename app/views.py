# -*- encoding: utf-8 -*-

import os
import logging
import urllib
import hashlib
from flask import request, jsonify, make_response, abort
from app import app

# path to images in the container
BASE_PATH = os.environ.get("BASE_PATH", '/static/images/')
# hostanme of nxing server
HOSTNAME = os.environ.get("HOSTNAME")


@app.route('/image', methods=['POST'])
def save_image():
    """ Download image to host and return url to get it from
    """
    if not request.json or 'image_url' not in request.json or 'image_id' not in request.json:
        app.logger.dubug('Not enough data to serve the request!')
        abort(400)

    image_url = request.json['image_url']
    image_id = request.json['image_id']
    image_tag = request.json.get('image_tag', 'default')

    dir_path = '{0}/{1}'.format(BASE_PATH, image_tag)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    try:
        image = urllib.request.urlopen(image_url)
    except Exception as err:
        app.logger.error('Failed to open image, reason: {0}'.format(err))
        abort(400)

    hash_object = hashlib.sha256(str(image_id).encode('utf-8')).hexdigest()
    with open('{0}/{1}'.format(dir_path, hash_object), 'wb') as image_file:
        image_file.write(image.read())

    url = 'http://{0}/images/{1}/{2}'.format(HOSTNAME, image_tag, hash_object)
    return jsonify({'url': url}), 201


@app.route('/image/<image_tag>/<image_id>', methods=['GET'])
def get_image(image_tag, image_id):
    """ Get image url using image tag and id
    """
    url = 'http://{0}/images/{1}/{2}'.format(HOSTNAME, image_tag, image_id)
    return jsonify({'url': url}), 200


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
