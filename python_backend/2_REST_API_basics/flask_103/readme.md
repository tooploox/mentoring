# Flask REST API basics

This lesson will guide you to learn how to upload a file to server
and access uploaded file to perform some basic operations.
Purpose of this lesson is to create the following endpoints:


* `Image conversion` - convert uploaded image to grayscale 
  and return processed image.
* `Image information` - retrieve basic image information and return to user.
  Basic image data:

    - width,
    - height,
    - color mode,
    - file size.


General information on how to proceed with exercises [here](../../readme.md).

## Resources

Upload a file to server: 
[File upload tutorial video](https://www.youtube.com/watch?v=Y82XKGKUtrU)

Send file from server: 
[File download tutorial video](https://www.youtube.com/watch?v=WICXiCtXX5U)


## Prerequisites

Details on how to setup the exercise can be 
found [here](../../readme.md#exercise-setup).

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

#### Use script

Use provided makefile commands.

Make commands are described in [python backend readme](../../readme.md#script-execution).

#### Run unit tests and ensure they pass.

Run the following command from current (`flask_101`) directory:

    make test


## Success conditions

This exercise does not require mentor's assistance, 
but you are not forbidden to do so should you need help :)

Details in [python backend readme](../../readme.md#exercise-success-conditions).
