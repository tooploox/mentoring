# Flask REST API basics

This lesson will guide you to learn how to create flask API.
Purpose of this lesson is to create an endpoint, run your flask app 
and make a request to your endpoint to verify it's working.

## Resources
Video tutorial on how to create a flask app:

    https://www.youtube.com/watch?v=mqhxxeeTbu0

## Prerequisites

In order to start this tutorial, you need a virtual environment, activate it,
install required modules and run solution check script (after you write code).
You can run the following commands manually, or execute provided script.

### Manual exercise setup
Create a virtual environment:

    python -m venv venv

Activate virtual environment
    
    . venv/bin/activate


Install required python modules by running:

    pip install -r requirements.txt

### Script execution
This assumes you understang how the virtual environment is setup 
and how to install necessary python modules (via `pip`)

    ./create_venv.sh

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

### 1. Exercise check is successful (Unit tests pass).
### 2. Your code is reviewed and approved.
### 3. (?) Your knowledge was checked by mentor.