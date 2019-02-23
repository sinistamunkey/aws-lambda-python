# aws-lambda

[![Codeship Status for sinistamunkey/aws-lambda-python](https://app.codeship.com/projects/4e953ee0-19ac-0137-b96c-1a1a0859fc7b/status?branch=master)](https://app.codeship.com/projects/328478)

AWS Lambda provides a simple Flask wrapper to allow you develop a simple AWS Lambda handler locally and access it via RESTful commands.

## Usage

You will need to structure your new application accordingly to be able to work with this container as it relies on certain files being in the right place.

```
.
+-- src
|   +-- lambda_handler.py   
+-- dev-requirements.txt
+-- docker-compose.yml
+-- Dockerfile
+-- requirements.txt 
```

Next you will need to ensure you use the correct docker image for your work, currently two tags are supported

- 2.7-onbuild
- 3.7-onbuild

**Dockerfile**
```
FROM sinistamunkey/aws-lambda-python:3.7-onbuild
```

The **lambda_handler.py** is the entry point for your lambda application and any of your custom code will be in here and reference your own libraries.

Be sure to keep all other modules and classes for your handler within **src**, for example:-

```
.
+-- src
|   +-- lambda_handler.py  
|   +-- services
    |   +-- __init__.py
    |   +-- client.py
```

While **docker-compose.yml** isn't required, it's helpful to have to make running your service a bit easier if you like.

**docker-compose.yml**
```
version: '3'
services:

  app:
    build: .
```

Finally, it is required to have both **dev-requirements.txt** and **requirements.txt**, even if you don't have any development requirements it will cause an error if it doesn't exist.

**dev-requirements.txt**
```
pytest
-r requirements.txt
```

**requirements.txt**
```
requests
```

## Notes

This is not meant to fully replicate an AWS Lambda instance and there are far better services for this, for example [localstack](https://github.com/localstack/localstack) but I found this approach helpful when working with Lambda handlers being communicated with by API Gateways.