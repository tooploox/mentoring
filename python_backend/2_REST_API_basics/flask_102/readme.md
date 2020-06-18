# Flask REST API passing parameters

This lesson will guide you to learn how to pass path arguments
in the url and perform basic operations on arguments.

General information on how to proceed with exercises
can be found [here](../../readme.md).

## Resources
Tutorials on how to use url and path parameters in flask app:

Query parameters:

[Youtube tutorial](https://www.youtube.com/watch?v=yNjn_c_ovIY)

[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data)
    
Path parameters:
    
[Youtube tutorial](https://www.youtube.com/watch?v=f085KDOy43k)

[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

## Prerequisites

Details on how to setup the exercise can be 
found [here](../../readme.md).

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
### 6. Check your solution

#### Use script

Execute provided bash script:

    ./check_solution.sh

This script may not only execute unit tests, but also perform other checks
(like ensure you are using a virtual environment).
#### Run unit tests and ensure they pass.

Run the following command from current (`flask_102`) directory:
    
    . venv/bin/activate
    python -m unittest -v
    
    

## Success conditions

Details in main python track [readme](../../readme.md)
