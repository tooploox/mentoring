# Flask tutorial 102

This lesson will guide you to learn how to pass path arguments
in the url and perform basic operations on arguments.

## Resources
Tutorials on how to use url and path parameters in flask app:

Query parameters:

    [Youtube tutorial](https://www.youtube.com/watch?v=yNjn_c_ovIY)
    [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data)
    
Path parameters:
    
    [Youtube tutorial](https://www.youtube.com/watch?v=f085KDOy43k)
    [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

## Prerequisites

Install required python modules by running:

    pip install -r requirements.txt

## Tasks

### 1. Define a BMI calculation endpoint ``/bmi/``
    It should accept weight (kg) and height (m) as url parameters.
### 2. Endpoint should return a BMI factor
    Return dictionary with `BMI` key and BMI float value, 
    rounded to 2 decimal places.
### 3. Validation
    Endpoint should validate both weight and height arguments.
### 4. Create a second endpoint ``/bmi2/``.
    The endpoint should accept height and weight arguments as path arguments.
### 5. Error handling
    In case of invalid/missing arguments the endpoint 
    should return ``BadRequest`` response.
### 3. Run unit tests and ensure they pass.

Use provided bash script:

    ./run_tests.sh

or run the following command from current (`flask_102`) directory:
    
Pytest:

    PYTHONPATH=../../../ pytest -v

Unittest:

    PYTHONPATH=../../../ python -m unittest -v
    

## Success conditions

### 1. Unit tests pass.
### 2. Your code is reviewed and approved.
### 3. (?) Your knowledge was checked by mentor.