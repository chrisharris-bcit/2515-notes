"""
API - Application Programming Interface

(Web) API - a set of related URLs (each URL is referred to as an 'endpoint') that return some (usually JSON) data

e.g.
https://jsonplaceholder.typicode.com/ (doesn't return JSON data)

https://jsonplaceholder.typicode.com/posts --> JSON data about 'posts'

https://jsonplaceholder.typicode.com/users --> JSON data about users

View data using:
    - a browser
    - a client app (Bruno, Insomnia, Postman)

HTTP - hypertext transfer protocol

Methods (options for sending and receiving data)

    GET             get a resource
    POST            create a resource (e.g. row in a db)
    PUT             update a(n existing) resource
    DELETE          delete a resource

    CRUD
        create -> POST
        read -> GET
        update -> PUT
        delete -> DELETE

Notes: APIs are 'stateless' - the server-side application does not remember what, for example, requests were made, any application state, etc. It simply returns data (from a db) or pass data (to a db)

Terminology: Idempotent 

From MDN: An HTTP method is idempotent if the intended effect on the server of making a single request is the same as the effect of making several identical requests.

    Method                      Idempotent
    GET                         YES
    POST                        NO
    PUT                         YES
    DELETE                      YES

    example of a POST request

        POST  { "username": "Chris", ... }
            creates a new row in the db
                ID: 1, USERNAME: Chris

        POST  { "username": "Chris", ... }
            creates another new row in the db
                ID: 2, USERNAME: Chris    

Statuses

    100s    Informational
    200s    Success (200)
    300s    Redirects (301)
    400s    Client Error (404, 401)
    500s    Server-Side/Application Error (500, 502, 503)

HTTP Request Structure
Request Line      ← method + path + version
Headers           ← metadata (key: value pairs)
                  ← blank line
Body (optional)   ← data sent to the server

example headers (they tell server things about the client)
    Content-Type      what type of data they are sending (JSON)
    Accept            what type of data they understand (JSON)

example body (for a POST, PUT, DELETE)

    {
        "username": "Tom",
        ...
    }

HTTP Response Structure
Status Line       ← version + status code + reason
Headers           ← metadata
                  ← blank line
Body              ← data returned by the server

"""

"""
Flask is a library that allows us to create backend (or full-stack) APIs/Web Servers

Two simpler alternatives for making requests are:
    requests (library)
    httpx (library)

Example:
    uv init
    uv add requests
"""
# import requests

# response = requests.get('https://jsonplaceholder.typicode.com/users')

# if response.status_code == 200:
#     data = response.json() # get the data from the HTTP response header and converts it to a python dictionary/list
#     print(data)

"""
Example Flask App:

    Steps:
    1. Create a folder
    2. uv init
    3. uv add flask
    4. check that your virtual env is activated, run:

        .venv/Scripts/activate

        ASIDE: if you get an error containing ~"not allowed to run scripts" you can run:

        Set-ExecutionPolicy Bypass -Scope CurrentUser
"""

"""
Simple version of how to create a Flask app
"""
from flask import Flask, render_template, request

app = Flask(__name__) 

# Define endpoints (aka routes)
# endpoints are defined by functions with decorators

# @app.get, @app.post, ..., OR @app.route (which can handle all request methods)

# respond to get requests to the root URL (http://localhost:5000)
@app.get('/test')
def test():
    return "Test"
    """
    data = {}
    return render_template('test.html', data)
    """

@app.get('/') 
def home(): # the name of the function can be anything
    # return "Home"
    return { "course": "ACIT2420", "difficulty": "easy" }
    """
    return {
        "username": "Paul",
        "grade": 100
    }

    return [
        {},
        {}
    ]
    """

if __name__ == '__main__':
    app.run()

"""
In Bruno/Browser, make a GET request to:
    http://localhost:5000
    http://localhost:5000/test

"""