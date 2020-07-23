# Flask learning track

## Exercises howto

- fork the repo in Github as a private repository (?), 
- create branch, e.g. <your_name>_<exercise_name> , 
- implement,
- test,
- create PR to YOUR repository, add the mentor as a reviewer.

## Exercise setup

In order to start an exercise, you need a virtual environment, activate it,
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
This assumes you understand how the virtual environment is setup 
and how to install necessary python modules (via `pip`)

#### Clean working directory
Removes virtual environment directory.

    make clean

#### Create virtual environment
Creates virtual env, activates it and installs requirements.

    make create

#### Execute unit tests
Runs unit tests

    make test

#### All-in-one command
Performs all above steps.

    make all

is equal to

    make clean create test



## Exercise success conditions

### 1. Exercise check is successful (unit tests pass).
### 2. Your code is reviewed and approved.
### 3. Your knowledge was checked by mentor (if not stated otherwise).

## Tutorials list

### 1. REST API Basics
#### Flask 101

This tutorial shows how to create a flask app with a basic API endpoint.
[Exercise details](2_REST_API_basics/flask_101/readme.md).

#### Flask 102

Learn how to access query and path parameters passed in the url.
[Exercise details](2_REST_API_basics/flask_102/readme.md).

### x. Flask uploading file to server
``(Work in progress)``

### x. Flask downloading file from server
``(Work in progress)``

### x. Flask authentication and authorization
``(Work in progress)``

### x. Flask Page Templating basics
``(Work in progress)``