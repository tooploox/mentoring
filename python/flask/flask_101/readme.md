# Flask tutorial 101

This lesson will guide you to learn how to create flask API.
Purpose of this lesson is to create an endpoint, run your flask app 
and make a request to your endpoint to verify it's working.

## Resources
Video tutorial on how to create a flask app:

    https://www.youtube.com/watch?v=mqhxxeeTbu0

## Prerequisites

Install required python modules by running:

    pip install -r requirements.txt

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

### 6. Run unit tests and ensure they pass.
Use provided bash script:

    ./run_tests.sh

or run the following command from current (`flask_101`) directory:
    
Pytest:

    PYTHONPATH=../../../ pytest -v

Unittest:

    PYTHONPATH=../../../ python -m unittest -v
    

## Success conditions

### 1. Unit tests pass.
### 2. Your code is reviewed and approved.
### 3. (?) Your knowledge was checked by mentor.