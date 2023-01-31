import json

# Importing JSON with load
with open('data\\posts-100.json', 'r') as f:
    posts_json = json.load(f)
print(type(posts_json))
# How many objects in json file?
print(len(posts_json))
# Returns the first object
print(posts_json[0])
# Returns the number of attributes in the first onject
print(len(posts_json[0]))
# Print a specific columns for a specific object (i.e. this is the first object)
print(posts_json[0]['Id'], posts_json[0]['Title'])


# # Importing JSON with loads
json_original = """{
        "Id": 5,
        "PostTypeId": "1",
        "CreationDate": "2014-05-13T23:58:30.457",
        "Score": 9,
        "ViewCount": 448,
        "LastActivityDate": "2014-05-14T00:36:31.077",
        "Title": "How can I do simple machine learning without hard-coding behavior?",
        "Tags": "<machine-learning>",
        "AnswerCount": 1,
        "CommentCount": 1,
        "FavoriteCount": 1,
        "ClosedDate": "2014-05-14T14:40:25.950"
    }"""
json_loaded = json.loads(json_original)
print(json_loaded)
print(type(json_loaded))

# This is a pretty print of the JSON object
print(json.dumps(json_loaded, indent=2))

## Now sure I understand what's going on here
# this_tuple = ('one', 'two')
# this_list = ['one','two']
# print(type(this_tuple))
# print(type(this_list))

# json_tuple = json.dumps(this_tuple)
# json_list = json.dumps(this_list)
# print(json_tuple)
# print(json_list)
# print(json_tuple == json_list)
# print(type(json.loads(json_tuple)))
# print(type(json.loads(json_list)))

## DID NOT WORK
# import requests
# weather_query = "https://query.yahooapis.com/v1/public/yql?q=select item.condition from weather.forecast
# where woeid = 2487889&format=json&env=store://datatables.org/alltableswithkeys"
# weather_call = requests.get(weather_query)
# weather = json.loads(weather_call.text)
# print(weather['query']['results']['channel']['item']['condition']['temp'])