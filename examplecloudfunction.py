import datetime
import json
import logging

from flask import abort
from google.cloud import storage

storage_client = storage.Client()

BUCKET_NAME = '' # TODO(you) Fill this in with your bucket name


def cloud_function_name(request):  # TODO(you) - name this function appropriate when creating your Google Cloud Function
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    if request.method != 'POST':
        return abort(405)

    data = request.get_json()
    if not data:
        logging.info("No data for request: {}".format(request))
        abort(405)

    data = json.loads(data)
    logging.info(data)
    logging.info(dir(data))
    logging.info(data.keys())

    if 'name' not in data:
        return abort(405)
    if 'data' not in data:
        return abort(405)

    dt = datetime.datetime.utcnow()

    fp = str(data["name"]) + '.' + str(dt.year) + '.' + str(dt.month) + '.' + str(dt.day) + '.' + str(dt.hour) + '.' + str(dt.minute) + '.' + str(dt.second) + '.' + str(dt.timestamp()) + '.json'

    bucket = storage_client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(fp)
    blob.upload_from_string(json.dumps(data['data']))

    return fp
