 Late Show API
A Flask REST API for managing a Late Night TV show system with guest appearances, episodes, and user authentication.

 Features

JWT Authentication - Secure user registration and login
Guest Management - Track TV show guests and their occupations
Episode Management - Manage show episodes with dates and numbers
Appearance Tracking - Rate guest appearances on episodes (1-5 scale)
PostgreSQL Database - Robust data persistence
MVC Architecture - Clean, organized code structure

 Tech Stack

Backend: Flask, Flask-SQLAlchemy, Flask-Migrate
Authentication: Flask-JWT-Extended
Database: PostgreSQL
Password Security: Werkzeug password hashing
Environment Management: python-dotenv

 Prerequisites
Before running this application, make sure you have:

Python 3.12+
PostgreSQL installed and running
Pipenv for dependency management

 Installation & Setup
1. Clone the Repository
bashgit clone https://github.com/Kaarr21/late-show-api-challenge.git
cd late-show-api-challenge
2. Install Dependencies
bashpipenv install flask flask-sqlalchemy flask-migrate flask-jwt-extended psycopg2-binary python-dotenv
pipenv shell
3. Database Setup
Create a PostgreSQL database:
bash# Using PostgreSQL command line
createdb late_show_db

# Or using psql
psql -U postgres
CREATE DATABASE late_show_db;
\q
4. Environment Configuration
Create a .env file in the project root:
bashDATABASE_URI=postgresql://username:password@localhost:5432/late_show_db
JWT_SECRET_KEY=your-super-secure-secret-key-here
Replace username and password with your PostgreSQL credentials.
5. Database Migration
bashexport FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
6. Seed the Database
bashpython server/seed.py
This creates sample data:

User: username karoki, password Karokin35!
3 guests (John Doe, Jane Smith, Elon Musk)
3 episodes
3 appearances with ratings

7. Run the Application
bashflask run
The API will be available at http://localhost:5000

 Testing with Postman
1. Import Collection
Import the late-show-api.postman_collection.json file into Postman.
2. Test Authentication Flow

Register: Use the "Register" request to create a new user
Login: Use the "Login" request to get your JWT token
Copy Token: Copy the access_token from the login response
Set Variable: In Postman, create a variable jwt_token and paste your token

3. Test Protected Routes

Create Appearance: Uses {{jwt_token}} variable automatically
Delete Episode: Requires authentication

4. Test Public Routes

Get Episodes: No authentication needed
Get Guests: No authentication needed
Get Episode by ID: No authentication needed

Security Features

Password Hashing: Uses Werkzeug's secure password hashing
JWT Tokens: Stateless authentication with configurable expiration
Input Validation: Server-side validation for all inputs
Rating Validation: Appearance ratings must be between 1-5
Database Constraints: Unique usernames, non-null fields
