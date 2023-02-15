from flask import Flask
from redis import StrictRedis

app = Flask(__name__)

redis_client = StrictRedis(host='127.0.0.1', port=63791, db=3)  # for local
# redis_client = StrictRedis(host='redis', port=6379, db=0)  # for Docker


@app.route("/flask/<key>", methods=["GET"])
def get_one_value(key):
    """ function to get one key:value """
    try:
        value = redis_client.get(key)
        if not value:
            return {'error': 'no such key available, Does not Exist'}
        return {key: str(value)}
    except Exception as e:
        return {'error': str(e)}


@app.route("/flask/<key>", methods=["PUT"])
def set_one_value(key):
    """
    function to create one key:value in db.Redis.
    Type of key would be STRING
    """
    try:
        redis_client.set(key, 'value') # 'string' type
        # redis_client.sadd(key, 'value')  # 'set' type
        return {key: 'created'}, 201
    except Exception as e:
        return {'error': str(e)}

