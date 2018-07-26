[![Build Status](https://travis-ci.org/PrincesaTyne/my-diary.svg?branch=api)](https://travis-ci.org/PrincesaTyne/my-diary)

my-diary

An on-line journal where users can pen down their thoughts and feelings.

https://princesatyne.github.io/my-diary/


Features
A can do the following:
Sign up
Login
Create a diary entry
Add a title to the diary entry
View diary entries
Edit a diary entry


API resources

|HTTP Method |Endpoint |Functionality |
|----------|----------|----------|
|GET |api/v1/entries |Fetch all entries |
|GET |api/v1/entries/entryId |Fetch a single entry |
|POST |api/v1/entries |Create an entry |
|PUT |api/v1/entries/entryId |Modify an entry |
|DELETE |api/v1/entries/entryId |Remove an entry |


Requirements
Python 3+, pip, virtual environment
