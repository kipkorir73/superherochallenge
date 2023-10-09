# SuperHeroes API

## Description

This project is a Flask-based API for tracking heroes and their superpowers. It provides endpoints to manage heroes, powers, and their relationships. Additionally, there is a fully built React frontend application for testing the API's functionality.

## Project Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:VictorOroo/SuperHeroesNew.git
Create a virtual environment (optional but recommended):

bash
Copy code
pipenv install
Install dependencies for the Flask backend:

bash
Copy code
pipenv install flask
pipenv install sqlalchemy
pipenv install flask-sqlalchemy
pipenv install flask-migrate
Install dependencies for the React frontend:

bash
Copy code
npm install --prefix client
# Usage
You can run the Flask API on localhost:5555 by running:

bash
Copy code
python app.py
You can run the React app on localhost:4000 by running:

bash
Copy code
npm start --prefix client


## Database Setup
This project uses a database to store heroes, powers, and their relationships. You need to set up the database by creating the necessary tables and seed data:

## Create the database tables and seed data by running:


flask db upgrade
python app/seed.py
If you encounter issues with the provided seed file, you can generate your own seed data to test the application.

## Models
The project includes the following models:

Hero: Represents a hero with a name and super name.
Power: Represents a superpower with a name and description.
HeroPower: Represents the relationship between heroes and powers, including the strength of the power.
The models have relationships set up to connect heroes and powers through the HeroPower model.

## Validations
The project includes validations for the HeroPower and Power models:

# HeroPower:

strength must be one of the following values: 'Strong', 'Weak', 'Average'
Power:

description must be present and at least 20 characters long
API Routes
The API provides the following routes:

GET /heroes: Get a list of heroes in JSON format.
GET /heroes/:id: Get details of a hero by ID in JSON format.
GET /powers: Get a list of powers in JSON format.
GET /powers/:id: Get details of a power by ID in JSON format.
PATCH /powers/:id: Update the description of a power by ID.
POST /hero_powers: Create a new relationship between a hero and a power.
Please refer to the code challenge description for more details on the expected JSON responses for each route.

## Contact Information
For any questions, suggestions, or contributions, you can contact:

Name: Collins Kipkorir
Email: kipkorirc583@gmail.com
## License
Copyright (c) 2023 Collins Kipkorir.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.# superherochallenge
# superherochallenge
