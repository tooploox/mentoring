# Flask REST API basics

This lesson will guide you to learn how to upload files to server
and perform some basic operations on that files.
Purpose of this lesson is to create endpoint that will provide functionality:


* `Image conversion` - scale uploaded image if scale value is provided and save
  scaled image as scaled_<image_name>.
* `Image information` - retrieve basic image information and return to user.
  Basic image data:

    - size = [width, height],
    - color mode,
    - file format.


General information on how to proceed with exercises [here](../../readme.md).

## Resources

Upload a file to server: 
[File upload tutorial video](https://www.youtube.com/watch?v=Y82XKGKUtrU)

Send file from server: 
[File download tutorial video](https://www.youtube.com/watch?v=WICXiCtXX5U)

Flask-Uploads [documentation](https://pythonhosted.org/Flask-Uploads/)

## Prerequisites

Details on how to setup the exercise can be 
found [here](../../readme.md#exercise-setup).

## Tasks

### 1. Create a flask app (following the tutorial)
### 2. Define the endpoint ``/``
### 3. Endpoint should return a dictionary with `status` key and value `ok`.
### 4. Create an endpoint ``/upload``. 

#### Description
This endpoint's GET method should return a prompt message that should suggest posting the files.
Any returned message should be ok.
Endpoint should accept multiple files on POST method.

If `scale` keyword is provided, uplaoded images should be scaled according to the scale factor
and saved with changed filename `scale_<filename>` in addition to original file.

Endpoint should return information on uploaded files as follows:

    response = {
        <filename_1>: {
            'message': message  # file upload success message
            'data': {
                'mode': mode,
                'format': format,
                'scale': scale,  # if scale provided
                'size': size_after_scaling  # if scale provided
            }
        }
    }

#### Flask app configuration
    
Uploaded files should be stored in an upload folder.
There should be a size limit for an uploaded file.
Let's set the limit for file to 450 kB for test purposes.
Currently provided files are:

    - data/mayan_calendar.jpg - 476 kB,
    - data/mezoamerican_figures.jpg - 110 kB


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
