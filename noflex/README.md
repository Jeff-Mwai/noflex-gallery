# NOFLEX GALLERY

#### Author: [Jeff-Mwai](https://github.com/Jeff-Mwai)

* Link to live site: [Gallery-Hub]()

## Description
Noflex gallery is an application made sorely for the purpose of displaying my photos. Other people can also see the photos when they visit the site, and the user can click on the image to view the details of an image.

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Jeff-Mwai/noflex-gallery
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## Bugs

* There are no known bugs at the moment

        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 
* Postgresql 
* Boostrap
* HTML


## Support and contact details
 Incase you have any questions or you would like to contribute, kindly reach me through my email at: jeffmwai3@gmail.com

### License

* [[License: MIT]](LICENCE.md) <Jeff-Mwai>               