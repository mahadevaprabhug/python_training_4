"""
In this release,
1. We made one endpoint for all get/post/put
2. We supported update record

So, finally, using below end point we can GET/POST/PUT/DELETE
    End Point: http://127.0.0.1:5000/mydbapi
"""

# -------
# Create App
#########
import flask
my_rest_api_app = flask.Flask(__name__) # Automatically file name will come
####################


# -------
# END POINT: URL http://127.0.0.1:5000/mydbapi mapped to route("/mydbapi")
#########
@my_rest_api_app.route("/mydbapi", methods=["GET", "POST", "PUT", "DELETE"])
def my_db_api_function():
    if flask.request.method == "GET":
        """
        Send all records
        """
        import sqlite3
        my_db_connection = sqlite3.connect("my_database.sqlite3")
        my_db_cursor = my_db_connection.cursor()
        my_db_cursor.execute("SELECT * FROM MY_TABLE")
        my_db_result = my_db_cursor.fetchall()
        return flask.jsonify(my_db_result)
    elif flask.request.method == "POST":
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
        if records_count is not None:  # means record already present
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
    elif flask.request.method == "PUT":
        """
        Assume end user is sending some record for update.
        We inform end user to send record in {"IP": '', "PICS": ""}

        Our Plan:
        Task-1: Get record sent by end-user
        Task-2: Check whether record already present
        Task-3: Update record to database
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
        if records_count is None:  # means record NOT present
            my_message = flask.jsonify({"message": "Record Not Present To Update"})
            return flask.make_response(my_message, 404)
        else:
            my_query = f"""
            UPDATE MY_TABLE
            SET
            PICS = '{img}'
            WHERE
            IP = '{ip}'
            """
            my_db_cursor.execute(my_query)
            my_db_connection.commit()
            my_db_connection.close()
            my_message = flask.jsonify({"message": "Record UPDATED"})
            return flask.make_response(my_message, 201)
        #########

    elif flask.request.method == "DELETE":
        """
        Assume end user is sending some record for delete.
        We inform end user to send record in {"IP": '', "PICS": ""}

        Our Plan:
        Task-1: Get record sent by end-user
        Task-2: Check whether record already present
        Task-3: Delete record to database
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
        if records_count is None:  # means record NOT present
            my_message = flask.jsonify({"message": "Record Not Present To Delete"})
            return flask.make_response(my_message, 404)
        else:
            my_query = f"""
            DELETE FROM MY_TABLE
            WHERE
            IP = '{ip}'
            """
            my_db_cursor.execute(my_query)
            my_db_connection.commit()
            my_db_connection.close()
            my_message = flask.jsonify({"message": "Record DELETED"})
            return flask.make_response(my_message, 201)
        #########

####################

# -------
# Run builtin server
#########
my_rest_api_app.run() # Default IP: 127.0.0.1, port = 5000
# my_rest_api_app.run(host='', port='')
####################
