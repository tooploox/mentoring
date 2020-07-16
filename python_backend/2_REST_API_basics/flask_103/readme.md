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
`TODO point to correct videos`

Video tutorial on how to create a flask app: 
[video](https://www.youtube.com/watch?v=mqhxxeeTbu0).

## Prerequisites

Details on how to setup the exercise can be 
found [here](../../readme.md).

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

Execute provided bash script:

    make check

This script may not only execute unit tests, but also perform other checks
(like ensure you are using a virtual environment).
#### Run unit tests and ensure they pass.

Run the following command from current (`flask_103`) directory:

    make check


## Success conditions

Details in [main python track readme](../../readme.md).
