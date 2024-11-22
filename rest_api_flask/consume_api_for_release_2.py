"""
'requests': library for working with APIs
"""

print("GET: Get all the records from database")
print("-"*20)
# --------------

try:
    import requests
    my_api_response = requests.get("http://127.0.0.1:5000/getdbdata")
    my_api_data = my_api_response.json()
    print(my_api_data)
    print("type of my_api_data: ", type(my_api_data))
except Exception as e:
    print("Error details:", e, end="\n\n")
    print("\n Not able to access API. \n Please check rest-api-file/server is running?? ")
    exit()

print("#"*40, end="\n\n")
###################################

print("POST: Add new record to database")
print("-"*20)
# --------------

try:
    import requests
    my_api_response = requests.post("http://127.0.0.1:5000/postdbdata",
                                    json={
                                        "IP":"124.124.124.124",
                                        "PICS": "abc.jpg"
                                    }
                                    )
    print("Status Code:", my_api_response.status_code, end="\n\n")

    my_api_data = my_api_response.json()
    print("my_api_data:", my_api_data, end="\n\n")

    print("type of my_api_data: ", type(my_api_data), end="\n\n")

except Exception as e:
    print("Error details:", e, end="\n\n")
    print("\n Not able to access API. \n Please check rest-api-file/server is running?? ")
    exit()

print("#"*40, end="\n\n")
###################################
