# basic_product_api
## Introduction
CRUD APIs for product and product list using Django Rest Framework
DRF Token authentication used for user login

## Tech Stack
Python-Django, DRF, SQLite3

## Steps to download and run the django application
Create Virtual Environment variable in your local repository where you want to clone/download the application

### Steps to create and activate virtual environment variable
`virtualenv -p python3 <venv>`<br/>
`source <venv>/bin/activate`

- After creating a virtual environment variable and activating it, Download the zip file or use git clone to place the application beside the created virtual environment variable (<venv> - (while creating variable name can be anything custom))

- Follow the commands below to install the dependencies and run on the local server ('127.0.0.1:8000')

`cd basic_product_api/`<br/>
`pip install -r requirement.txt`<br/>
`python manage.py makemigrations`<br/>
`python manage.py migrate`<br/>
`python manage.py createsuperuser`
- Fill in the required details for creating superuser

`python manage.py runserver`
- This will run the django application on local server ('127.0.0.1:8000')

## Accessing the URLs
- You can use the browser to get all the URLs list by visiting the URL `http://127.0.0.1:8000`

- You can also use the .json file given in this repository
- Import the downloaded .json file in your local postman collection
- All the URLs like user-login and CRUD product is provided
- For GET method URLs, use the URL params to send type as `?type=<device_type>`

# Thank You
