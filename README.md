# image_tagger

image_tagger is a simple tagging application that allows images 
to be uploaded with tags and then searched 


## Installation

Set up a Python3 Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

Install django and django-rest-framework on the virtual environment
```bash
pip install django 
pip install djangorestframework
```

Then clone this repository to your system and run the migration 
```bash
cd config/
python manage.py migrate
```

Next create a superuser for the project 
```bash
python manage.py createsuperuser --email <email> --username <username>
```

Finally create an auth token to use with the API
```bash
python manage.py drf_create_token <username>
```


## Usage
GET Request

```bash
curl -X POST http://localhost:8000/images/ -H 'Authorization: Token <API_TOKEN>'\
``` 

GET specific id
```bash
curl -X POST http://localhost:8000/images/<id>/ -H 'Authorization: Token <API_TOKEN>'\
``` 

POST Request
```bash
curl -X POST http://localhost:8000/images/ -H 'Authorization: Token <API_TOKEN>' -H 'Content-Type: application/json' \
-F "title=<IMAGE_TITLE>"\  
-F "image=@<IMAGE_PATH>;type=image/jpg"\
-F "tags=[TAGS, TAGS]" 
``` 

PATCH Request - modify specific field
```bash
curl -X PATCH http://localhost:8000/images/ -H 'Authorization: Token <API_TOKEN>' -H 'Content-Type: application/json' \
-F "tags=[NEW_TAGS, NEW_TAGS]" 
``` 

PUT Request - modify all fields of existing image
```bash
curl -X PATCH http://localhost:8000/images/ -H 'Authorization: Token <API_TOKEN>' -H 'Content-Type: application/json' \
-F "title=<IMAGE_TITLE>"\  
-F "image=@<IMAGE_PATH>;type=image/jpg"\
-F "tags=[TAGS, TAGS]" 
``` 

Searching - search existing images by a tag
```bash
curl -X POST http://localhost:8000/images?search=<SEARCH_TERM> -H 'Authorization: Token <API_TOKEN>'\
``` 
