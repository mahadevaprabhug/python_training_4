"""
In this release,

we created 2 API

1 API: end user can get all the records
    API-1 End Point: http://127.0.0.1:5000/getdbdata

2nd API: end user can add new record to our database table
    API-2 End Point: http://127.0.0.1:5000/postdbdata

"""

# -------
# Create App
#########
import flask
my_rest_api_app = flask.Flask(__name__) # Automatically file name will come
####################

# -------
# END POINT - 1: URL http://127.0.0.1:5000/getdbdata mapped to route("/getdbdata")
#########
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_function():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
####################

# -------
# END POINT - 2: URL http://127.0.0.1:5000/postdbdata mapped to route("/postdbdata")
#########
@my_rest_api_app.route("/postdbdata", methods=["POST"])
def post_db_data_function():
    """
    Assume end user is sending new record.
    We inform end user to send new record in {"IP": '', "PICS": ""}

    Our Plan:
    Task-1: Get new record sent by end-user
    Task-2: Check whether record already present
    Task-3: Add new record to database
    """
    # --------
    # Task-1: Get new record sent by end-user
    # --------
    new_record = flask.request.get_json()
    # new_record will be like {"IP": '', "PICS": ""}

    # ip = new_record["IP"]
    # OR
    ip = new_record.get("IP")

    img = new_record.get("PICS")
    #########

    # --------
    # Task-2: Check whether record already present
    # --------
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_query = f"SELECT * FROM MY_TABLE WHERE IP = '{ip}'"
    my_db_cursor.execute(my_query)
    records_count = my_db_cursor.fetchone()
    if records_count is not None: # means record already present
        my_message = flask.jsonify({"message": "Record Already Present"})
        return flask.make_response(my_message, 406)
    else:
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{img}')"
        my_db_cursor.execute(my_query)
        my_db_connection.commit()
        my_db_connection.close()
        my_message = flask.jsonify({"message": "New Record Added"})
        return flask.make_response(my_message, 201)
    #########

####################

# -------
# Run builtin server
#########
my_rest_api_app.run() # Default IP: 127.0.0.1, port = 5000
# my_rest_api_app.run(host='', port='')
####################
