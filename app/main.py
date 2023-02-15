from flask import Flask, request
from redis import StrictRedis
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# redis_client = StrictRedis(host='127.0.0.1', port=63791, db=3)  # for local
redis_client = StrictRedis(host='redis_flask', port=6379, db=0)  # for Docker


def check_if_exist(key):
    """
    perhaps there is no need to separate this function.
    function to check is key in DB
    :param key: key in DB
    :return: 1=exist, 0=no such key
    """
    return redis_client.exists(key)


@app.route("/")
def index():
    return {'home page': "flask API application, using Redis DB"}


@app.route("/flask/<key>", methods=["GET"])
def get_one_value(key):
    """ function to get one key:value """
    try:
        value = redis_client.get(key)
        if not check_if_exist(key):
            return {'error': 'no such key available, Does not Exist'}, 404
        return {key: str(value)}
    except Exception as e:
        # raise HTTPException(status_code=404, detail=str(e))
        return {'error': str(e)}, 500


@app.route("/flask/<key>", methods=["POST"])
def create_one_key(key):
    """
    function to create one key:value in db.Redis.
    Type of key would be STRING
    """
    try:
        redis_client.set(key, request.json["value"])  # 'string' type
        # redis_client.sadd(key, value)  # 'set' type
        return {key: 'created'}, 201
    except Exception as e:
        return {'error': str(e)}


@app.route("/flask/<key>", methods=["PUT"])
def update_one_value(key):
    """
    function to update value in db.Redis
    """
    try:
        if not check_if_exist(key):
            return {'error': 'no such key available, Does not Exist'}, 404
        redis_client.set(key, request.json["value"])  # 'string' type
        # redis_client.sadd(key, value)  # 'set' type
        return {key: 'updated'}, 201
    except Exception as e:
        return {'error': str(e)}


@app.route("/flask", methods=["GET"])
def get_all_keys():
    try:
        all_keys_response = []
        all_keys = redis_client.keys()
        print('__' * 29)
        # print('all_keys', all_keys)
        for key in all_keys:
            all_keys_response.append({key.decode(): redis_client.get(key).decode()})
        return all_keys_response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
