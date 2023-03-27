# Flask and SQLAlchemy Web Application

This is a simple Flask web application which implements a simple e-commerce website where users can view items sold by the website. It leverages SQLAlchemy library to manage a SQLite database named 'about.db' to store items sold by the website. The Flask framework is used to serve web page templates and handle user request routing.

## Key Features
- A SQLite database is created and managed with SQLAlchemy
- The `Item` class is mapped to an `items` table in the SQLite database
- There are two Flask routes: `home_page()` and `about_page()`
- The rendered template pages utilize Bootstrap framework for styling
- The `about_page()` connects to the database to retrieve all the items and display them

## Installation and Usage
- Clone the repository
- Create a virtual environment
- Install Flask and SQLAlchemy: `pip install flask sqlalchemy`
- In the terminal, export Flask application instance: `export FLASK_APP=app.py`
- In the terminal, create the database and its table: `flask shell`
- In the Python shell in the terminal run: `db.create_all()`
- To run Flask, type `flask run` in the terminal

## Routes
The application has two main routes:
- **Home Page**: (`http://localhost:5000/`) displays the website's homepage
- **About Page**: (`http://localhost:5000/about`) displays all the items in the website's database

## Contributors
- [Your Name](https://github.com/your-github-username)