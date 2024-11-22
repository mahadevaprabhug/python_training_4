"""
'requests': library for working with APIs
"""

print("Access weather API")
print("-"*20)
# --------------

import requests

weather_api_response = requests.get("https://demoqa.com/utilities/weather/city/bangalore")
weather_api_data = weather_api_response.json()
print(weather_api_data)
print(type(weather_api_data))

print("#"*40, end="\n\n")
###################################

print("GET db data")
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

print("#"*40, end="\n\n")
###################################
