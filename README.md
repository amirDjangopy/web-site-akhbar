This project is a news content management system (CMS) written using the Django framework in Python. It allows you to easily create, edit, and publish news articles.

Features

Easy to use interface: The system has a simple and intuitive user interface that makes it easy for anyone to use.

Complete news management: You can easily create, edit, and delete categories, tags, and news articles.

Automatic publishing: You can schedule news articles to be published at a future time.

Search engine friendly: The system is optimized for search engines, meaning your news articles will be easily found by users.

Secure: The system uses encryption and other security measures to protect your data.

Prerequisites

Python 3.7 or higher

Django 3.2 or higher

A PostgreSQL database

Installation

Clone this project using git clone:

git clone https://github.com/your-username/django-news-project.git 

Navigate to the project directory:

cd django-news-project 

Activate the Python virtual environment:

python -m venv venv 

Install the project's dependencies:

pip install -r requirements.txt 

Set up a PostgreSQL database.

Configure the database settings in the settings.py file.

Run the database migrations:

python manage.py migrate 

Run the development server:

python manage.py runserver 

Usage

Go to http://127.0.0.1:8000/ in your browser.

To log in, use the username admin and the password password.

Once logged in, you will have access to the news administration panel.

