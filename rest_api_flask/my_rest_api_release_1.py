"""
Python for web development

We have many web frameworks in python
example
- flask
- django - MVT - Model View Template
- fastapi
many more
"""

"""
We are Discussing 'flask'

Using flask framework
1. Using flask framework we can develop websites
2. Using flask framework we can develop REST API
3. Using flask framework we develop micro services
"""

"""
We will discuss,
How to use flask framework to develop REST-API
"""

"""
Example to understand what is REST-API,
Suppose, we need to provide access to my_database to others/public
then how to provide access to my_database to others/public
 
ONE OPTION: We can provide credentials like username/password/db/host/port etc

This OPTION is limited
"""

"""
We got 2 options
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

both are called Architectures/Designs/Styles
both tells how to provide access to others

both tells introduce some INTERFACE in between out-app and others/public
our-app <--INTERFACE--> others/public

This INTERFACE is also called APPLICATION PROGRAMMING INTERFACE(API)

Both tells how to implement such INTERFACES

"""

"""
REST Came after SOAP
REST is easy implement
REST is popular
"""

"""
flask framework, already implemented REST architecture.
No need to implement, REST architecture from the scratch
- We JUST need to know, how to create REST-API using flask
"""

"""
We are planning provide complete/full access to our database with others.

complete/full access means?

- Creating new records
- Reading existing records
- Updating existing records
- Delete existing records
"""

"""
HTTP standard methods

POST:       Creating new records
GET:        Reading existing records
PUT/PATCH:  Updating existing records
DELETE:     Delete existing records
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
# Run builtin server
#########
my_rest_api_app.run() # Default IP: 127.0.0.1, port = 5000
# my_rest_api_app.run(host='', port='')
####################
