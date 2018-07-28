[![Build Status](https://travis-ci.org/PrincesaTyne/my-diary.svg?branch=api)](https://travis-ci.org/PrincesaTyne/my-diary)
[![Maintainability](https://api.codeclimate.com/v1/badges/49e1db25917a4fdd37b1/maintainability)](https://codeclimate.com/github/PrincesaTyne/my-diary/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/PrincesaTyne/my-diary/badge.svg?branch=api)](https://coveralls.io/github/PrincesaTyne/my-diary?branch=api)

## my-diary

An on-line journal where users can pen down their thoughts and feelings.


**Features**

A user can do the following:

Sign up

Login

Create a diary entry

Add a title to the diary entry

View diary entries

Edit a diary entry


**UI Interface**

Find the templates hosted on gh pages

https://princesatyne.github.io/my-diary/


**API**

Find the API at

https://dashboard.heroku.com/apps/my-diary23


**API resources**

|HTTP Method |Endpoint |Functionality |
|----------|----------|----------|
|GET |api/v1/entries |Fetch all entries |
|GET |api/v1/entries/entryId |Fetch a single entry |
|POST |api/v1/entries |Create an entry |
|PUT |api/v1/entries/entryId |Modify an entry |
|DELETE |api/v1/entries/entryId |Remove an entry |


**Requirements**

Python 3+, pip, virtual environment


**Installation**

Make a directory on your computer
```
$ mkdir my-diary
```

Initialize the directory
```
$ git init
```

Clone the project repository

$ git clone https://github.com/PrincesaTyne/my-diary.git

Create a virtual environment
```

$ pip install pipenv
```

Activate the virtual environment
```

$ pipenv shell
```

Run the development server
```

$ python run.py
```

The site is hosted at http://localhost:5000/


**Run Tests**

Install pytest
```

$ pip install pytest
```

Runs the tests
```

$ pytest
```
