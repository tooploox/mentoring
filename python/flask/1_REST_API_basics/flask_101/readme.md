# Flask REST API basics

This lesson will guide you to learn how to create flask API.
Purpose of this lesson is to create an endpoint, run your flask app 
and make a request to your endpoint to verify it's working.

General information on how to proceed with exercises [here](../../readme.md).

## Resources
Video tutorial on how to create a flask app: 
[video](https://www.youtube.com/watch?v=mqhxxeeTbu0).

## Prerequisites

Details on how to setup the exercise can be 
found [here](/python/flask/readme.md).

## Tasks

### 1. Create a flask app (following the tutorial)
### 2. Define the endpoint ``/``
### 3. Endpoint should return a dictionary with `status` key and value `ok`.
### 4. Run the app
### 5. Check the endpoint is working. Use one or more of the following methods:
    
    browser
    requests python module
    Postman
    curl
    Insomnia

### 6. Check your solution

### Use script

Use provided bash script:

    ./check_solution.sh

This script may not only execute unit tests, but also perform other checks
(like ensure you are using a virtual environment).
#### Run unit tests and ensure they pass.

Run the following command from current (`flask_101`) directory:
    
Pytest:

    PYTHONPATH=. pytest -v

Unittest:

    PYTHONPATH=. python -m unittest -v
    

## Success conditions

Details in [main python track readme](/python/flask/readme.md)
