from flask import Flask, request
from modules.database.src.database import Database
from modules.utils.src import rest_api_rescode
from modules.utils.src import db_rescode, flask_app_config

app = Flask(__name__)

pool_db = Database()


@app.route('/api/write_pool', methods=['POST'])
def write_pool():
    """
    POST API write pool data to pool database
    """
    client_data = None
    server_response = dict()
    status = str()
    retcode = rest_api_rescode.OK
    try:
        if request.is_json:
            client_data = request.get_json()
        res = pool_db.write_pool_to_db(client_data)
        if res == db_rescode.RES_WRITE_SUCCESS_INSERTED:
            status = "Inserted"
        if res == db_rescode.RES_WRITE_SUCCESS_APPEND:
            status = "Appended"
    except ValueError as e:
        status = str(e)
        retcode = rest_api_rescode.UNSUPPORTED_MEDIA_TYPE
    server_response.update({"status": status})
    return server_response, retcode


@app.route('/api/query_pool', methods=['POST'])
def read_pool():
    """
    POST API query quantile and length of
    list data corresponding to given poolId
    """
    client_data = None
    server_response = dict()
    res, quantile, len_list = str(), float(), int()
    retcode = rest_api_rescode.OK
    try:
        if request.is_json:
            client_data = request.get_json()
        quantile = pool_db.query_quantile_from_db(client_data)
        len_list = pool_db.query_len_list_from_db(client_data)
        res = "Success"
    except ValueError as e:
        res, quantile, len_list = str(e), None, None
        retcode = rest_api_rescode.UNSUPPORTED_MEDIA_TYPE
    server_response.update(
        {"status": res, "quantitle": quantile, "len_list": len_list})
    return server_response, retcode


if __name__ == "__main__":
    app.run(host=flask_app_config.APP_HOST, port=flask_app_config.APP_PORT)
