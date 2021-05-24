# cowryse-test
A python app that generates a key value pair of timestamp(the key) and a random Uuid(the value) on every request.

# Get started
use the comand `git clone https://github.com/Prometheo/cowryse-test.git` to clone this repo to your local enviroment

create a virtual enviroment using the python venv module(or any of your choice) `python -m venv your-env-name`

change directory to the cloned app with the command `cd cowryse-test`(on windows)

install the app requirements with the command `pip install -r requirements.txt`

start the development server with the command `python manage.py runserver`

head to your postman(or any tool you use n testing endpoints) and make a get request to `your-local-host/pairs/`
