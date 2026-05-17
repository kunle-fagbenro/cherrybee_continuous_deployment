#-------------------------------------------------------------------------------
# Use curl to send a GET request
brew install curl
curl https://jsonplaceholder.typicode.com/todos
# above is an example of a response that is not a web page
curl https://jsonplaceholder.typicode.com/todos | less
# to see less (use curl in your terminal and q to exit the URL)
curl -i https://jsonplaceholder.typicode.com/todos | less
# curl just represents the response body, add -i flag to see headers

#-------------------------------------------------------------------------------
# FLASK APP (creating the flask app)
# python library to create web server programs using python
# creating a minimal FLASK app
1. mkdir cherrybee_book_store
2. cd cherrybee_book_store
3. python -m venv cherrybee_book_store_venv 
4. source cherrybee_book_store_venv/bin/activate
5. pip install flask
6. pip freeze > requirements.txt
7. touch app.py
8. put the below in app.py
    # from flask import Flask
    # app = Flask(__name__)
    # if __name__ == "__main__":
        # app.run(port=5001, debug=True)

#-------------------------------------------------------------------------------
# RUNNING THE FLASK app
1. python app.py (from same directory as app.py)
2. curl http://127.0.0.1:5001/hello (from a new terminal tab)
3. error message. app does not know how to handle requests yet

#-------------------------------------------------------------------------------
# FLASK -Building GET Routes
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

1. run curl http://127.0.0.1:5001/hello on other terminal while the main still open
2. you should receive "Hello to you too"
3. create a new route that responds to requests sent with a GET method and PATH /books
4. open server and run curl on the other terminal

#--------------------------------------------------------------------------------
# TESTING ROUTES
1. pip install pytest
2. pip freeze > requirements.txt
3. mkdir tests
4. touch ./tests/test_app.py

# FIRST ROUTE TESTS
# one for the status code
# one for the response body
1. import sys
2. import os
3. sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
4. from app import app
5. def test_get_books_returns_a_200():
6. client = app.test_client()
7. response = client.get("/books")
8. assert response.status_code == 200
9. run pytest and test should pass
10. add a test for the response body

# CHALLENGE TDD a new request to GET/authors and pair programming to get quotes
1. All done first writing the test in test_app.py and making routes in app.py

#----------------------------------------------------------------------------------
# HTML
1. mkdir templates
2. cd templates
3. touch index.html
4. echo "<h1>Welcome to AceReads</h1>" > index.html
5. create a new route GET "/", return index.html and add render_template

#----------------------------------------------------------------------------------
# CSS
1. mkdir static
2. cd static
3. touch styles.css
4. add <link rel="stylesheet" href="/static/styles.css"> inside the head of your HTML

# CSS
1. mkdir css_practice
2. cd css_practice
3. touch index.html
4. copy provided HTML into it
5. touch styles.css (leave this empty for now)
6. open index.html

# CSS (STYLING WITHOUT WRITING CSS)
1. <link rel="stylesheet" href="https://cdn.simplecss.org/simple.css">
2. add the above into books amd index html in templates
3. use open books.html to see changes
4. add this to all your html and comment it out if not used

#----------------------------------------------------------------------------------
# PLAYWRIGHT
1. pip install pytest-playwright
2. pip freeze > requirements.txt
3. playwright install

# FIRST PLAYWRIGHT TEST
1. cd tests
2. touch test_landing_page_py 
3. add the provided code
4. now open your server in one terminal and run pytest in another
5. edit the provided code to work for books.html 
6. test failing (SPEAK TO COACH)

#----------------------------------------------------------------------------------
# AWS MANUAL DEPLOYMENT AND CONNECTING TO EC2
1. app is running now on 127.0.0.1 (accessible only from same machine)
2. in app.py add the host
3. app.run(host="0.0.0.0", port=5001, debug=True) 
4. follow steps to launch AWS instance
6. chmod 400 ~/.ssh/ola_cloud_deployment.pem
ssh -i ~/.ssh/ola_cloud_deployment.pem ec2-user@3.8.17.100
7. Above to SSH into your EC2 instance
8. mv ~/Downloads/cherrybee_cloud_deployment.pem ~/.ssh
9. above is to move your security key to ssh
10. 2 instances created one for ola (book_store) and cherrybee (cherrybee_book_store)
11. public ip address for ola: 3.8.17.100
12. public ip address for cherrybee: 3.8.167.155
13. chmod 400 ~/.ssh/cherrybee_cloud_deployment.pem
ssh -i ~/.ssh/cherrybee_cloud_deployment.pem ec2-user@3.8.167.155
14. scp -r -i ~/.ssh/cherrybee_cloud_deployment.pem \
app.py tests templates static requirements.txt \
ec2-user@3.8.167.155:~/cherrybee_book_store
15. run the above in cherrybee_book_store dir and ctrl D SSH first
16. cd cherrybee_book_store (SSH back into EC2)
17. ls
18. python --version (on local machine)
19. sudo dnf install -y python3.13 pip (on SSH EC2)
20. python3.13 -m venv cherrybee_book_store_venv
21. source cherrybee_book_store_venv/bin/activate
22. pip freeze > requirements.txt
23. python3.13 app.py (if error try pip install flask first)
23. http://3.8.167.155:5001, http://3.8.167.155:5001/books, http://3.8.167.155:5001/books.html, http://3.8.167.155:5001/change.html
24. when changes made, redeploy again to see this, SSH into EC2, cd into dir & open connection

#----------------------------------------------------------------------------------
# FLASK - CONNECTING TO A DATABASE
1. venv activated
2. pip install psycopg
3. pip freeze > requirements.txt

# MAKE A DATABASE AND A TABLE
1. createdb cherrybee_book_store
2. psql -h 127.0.0.1 cherrybee_book_store
3. create book table with 3 columns: id, title & author
4. create the DatabaseConnection Class (in lib)
5. create the Book Class (in lib)
6. create the BookRepository Class (in lib)
7. only __init__ and all methods needed for now

# FLASK - READING FROM A DATABASE
1. psql -h 127.0.0.1 cherrybee_book_store < cherrybee_book_store.sql
2. seed into the database with the above
3. Now the previous stuff in the app.py are now commented out.
4. paste the provided code in the app.py

# Passing Data into templates
1. update /books route so that books is passed into the book.html template
2. see the update in app.py

# Jinja Templates to replace hard-coded list of books
1. create a route called /team (see app.py)
2. create a new template called team.html
3. add contents into it, see team.html content in it

#-------------------------------------------------------------------------------------
# DOCKERISING THE BOOK STORE

1. install docker desktop
2. run

# write a dockerfile (recipe that tells docker how to build a container)
1. touch Dockerfile (in cherrybee_book_store)
2. add 

FROM python:3.13
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# create (build) an image
1. make sure your docker is running
2. docker build -t cherrybee_book_store
3. docker images

# create (run) a container
1. docker run -p 5001:5001 cherrybee_book_store

#----------------------------------------------------------------------------------
# DOCKERISING YOUR DATABASE

# create a docker network
1. docker network create cherrybee_book_store_network
2. docker network ls

# run a postgres container
1. rather than Dockerfile, pull a ready made image from docker hub
2. docker run \
  --name cherrybee_book_store_db \
  --network cherrybee_book_store_network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=cherrybee_book_store \
  -d postgres:17
3. docker ps

# connect to your postgres container
1. docker exec -it cherrybee_book_store_db psql -U postgres
2. \list
3. \q (to exit)

# run your migration file(s)
1. docker exec -i cherrybee_book_store_db psql -U postgres -d cherrybee_book_store < ./seeds/cherrybee_book_store.sql

# update your database connection string
1. change "postgresql://localhost/book_store" in database_connection.py
2. to "postgresql://postgres:password@cherrybee_book_store_db/cherrybee_book_store"
3. docker build -t book_store .

# run the app container on the same network
1. docker run \
  -p 5001:5001 \
  --network cherrybee_book_store_network \
  cherrybee_book_store

#----------------------------------------------------------------------------------
# DOCKERISED DEPLOYMENT
# getting your app and database running in containers on EC2

1. ssh -i ~/.ssh/cherrybee_cloud_deployment.pem ec2-user@3.8.167.155
2. install Docker on your EC2 instance
3. sudo dnf update -y
sudo dnf install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
newgrp docker
4. log out of EC2 (ctl + d)
5. ssh -i ~/.ssh/cherrybee_cloud_deployment.pem ec2-user@3.8.167.155
6. docker version
7. docker ps

# copy your project to EC2
1. back on your local machine cd to the your project folder
2. scp -r -i ~/.ssh/cherrybee_cloud_deployment.pem \
  *.py requirements.txt Dockerfile seeds templates static \
  ec2-user@3.8.167.155:~/cherrybee_book_store
3. this overwrites all previously copied
4. cd cherrybee_book_store
5. ls

# build and run everything
1. create network: docker network create cherrybee_book_store_network
2. run the postgres container
3. docker run \
  --name cherrybee_book_store_db \
  --network cherrybee_book_store_network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=cherrybee_book_store \
  -d postgres:17
4. run sql file to create books table and some entries
5. docker exec -i cherrybee_book_store_db psql -U postgres -d cherrybee_book_store < seeds/cherrybee_book_store.sql
6. build the image: docker build -t cherrybee_book_store .
7. run the app container:
docker run \
  -p 5001:5001 \
  --network cherrybee_book_store_network \
  cherrybee_book_store

#----------------------------------------------------------------------------------
# HTTP - POST REQUEST
# used to send data to a server, creating database entries. Made using FORM in browser
# or tool like curl
1. use curl to send a post request
2. curl -X POST https://jsonplaceholder.typicode.com/todos \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Buy milk",
       "completed": false,
       "userId": 1
     }'
3. if you enter the above in your terminal, you'll get back the below response
4. {
  "title": "Finish HTTP lesson",
  "completed": false,
  "userId": 1,
  "id": 201
}
5. if this worked, good but this is just a simulation, we need a new route to our app

# FLASK - building POST routes
1. aim here is to create new books

# adding a POST route
1. @app.route('/books', methods=['POST'])
2. note you can have both GET and POST routes with the same path (/books)
3. @app.route('/books', methods=['POST'])
def create_book():
  pass
4. above is an empty route

# grabbing the request body
1. # adds `request` to your existing import
from flask import Flask, request
2. @app.route('/books', methods=['POST'])
   def create_book():
    book_details = request.json
    print(book_details)
    return "created", 201
3. restart your app (python app.py)
4. run the below in another terminal
5. curl -X POST http://localhost:5001/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Book Title","author":"Author Name"}'
6. app shows it can handle a POST request and grab the requested body, but doesn't create a new book in the database

# writing a new book to the database (5 steps)
1. in BookRepository add a create method that'll save new books to database
note that my BookRepository works with instances of Book
def create(self, book):
    self._connection.execute(
        'INSERT INTO books (title, author) VALUES (%s, %s)',
        [book.title, book.author]
    )
    return None
2. make an instance of DatabaseConnection (in POST route)
@app.route('/books', methods=['POST'])
def create_book():
    # make a new database connection
    connection = DatabaseConnection()
    connection.connect()
    # make a new instance of BookRepository
    book_repository = BookRepository(connection)
    # get the request body
    book_details = request.json
    # my BookRepository expects an instance of Book, so make one here
    book = Book(title=book_details["title"], author=book_details["author"])
    # save the book
    book_repository.create(book)
    # return a 201, which means "created"
    return "created", 201
3. updated Book class:
  class Book:
  # books don't have an id until they are saved to the database
  # so we need a default value for id
  # and parameters with a default must come last
  # this change, means the `BookRepository` will no longer work as expected
  def __init__(self, title, author, id = None):
    self.id = id
    self.title = title
    self.author = author

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a Book
  def __repr__(self):
    return f"Book({self.id}, {self.title}, {self.author})"
4. New BookRepository all method
    # id is now the third argument
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["id"])
            books.append(item)
        return books
        
#--------------------------------------------------------------------------------
# FLASK and HTML - FORMS
# want users to create new books via nice form in their browser

# adding a FORM
1. FORM to have 2 field TITLE and AUTHOR and a SUBMIT button
2. <form method="POST" action="/books">
    <input type="text" name="title" placeholder="Title">
    <input type="text" name="author" placeholder="Title">
    <input type="submit" value="Submit">
  </form>

# updating your POST route
1. the POST route expects a json but we want form data
2. change book_details = request.json to
3. book_details = request.form

# redirecting (redering the template in POST route)
1. @app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    books = book_repository.all()  
    return render_template("books.html", books=books)

# redirecting (properly done way)
1. @app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

#-------------------------------------------------------------------------------
# TESTING FORMS
# playwright to interact with HTML form
1. navigate to the page the form is on 
   page.goto("https//localhost:5001/books")
2. grab and fill the first field. Title. using get_by_placeholder
   page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
3. grab author next
   page.get_by_placeholder("Author").fill("Geronimo")
4. pressing the submit button
   page.get_by_role("button", name="Submit").click()
5. write a new test to navigate to /books page, fills in form, submit it and    checks if new book in list of books

# in a new file called `test_create_new_book.py`

from playwright.sync_api import Page, expect

def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"

6. remember, 2 terminals, venv activated for both

#--------------------------------------------------------------------------------
# USING A TEST DATABASE 

# app creates and list books with some tests that affects the database
# solution is reset database before every test
# then write a test which modifies the database and that's undone b4 next test
# option of adding books in browser without deletion everytime tests run
# solve this by creating second database used only for testing

# RESETTING THE DATABASE
1. sql file that removes all books and re-populate with what we expect. put in seeds dir and call books.sql. put the below in the books.sql file
TRUNCATE table books;

INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');

2. add the seed method below to test_landing_page.py
   def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

# Creating and Using a test database
1. createdb cherrybee_book_store_test
2. psql -h 127.0.0.1 cherrybee_book_store_test
3. add tables
   CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
   );
4. import os (test_landing_page.py)
5. in database_connection.py
   DATABASE_NAME = os.getenv("DATABASE_NAME", "cherrybee_book_store_test")
6. python app.py (starting server with this uses test database)
7. DATABASE_NAME=cherrybee_book_store python app.py (server uses original DB)

#--------------------------------------------------------------------------------
# DOCKERISED DEPLOYMENT

# we go for non-sensitive env var and declare them in our dockerfile
# anytime app is running in docker, DATBASE_HOST will be our dockerised database
# DATABASE_NAME will be our dev database not test

# updating our Dockerfile
1. add 2 ENV lines and the rest stays the same
   FROM python:3.13
   ENV DATABASE_NAME="book_store"
   ENV DATABASE_HOST="postgres:password@book_store_db"
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   CMD ["python", "app.py"]
2. updated database_connection.py
   class DatabaseConnection:
    DATABASE_NAME = os.getenv("DATABASE_NAME", "book_store_test")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost") # <<< grab the new env var

    def __init__(self):
        self.connection = None

    # This method connects to PostgreSQL using the psycopg library. We connect
    # to localhost and select the database name given in argument.
    def connect(self):
        try:
            self.connection = psycopg.connect(
                # use the new env var
                f"postgresql://{self.DATABASE_HOST}/{self.DATABASE_NAME}",
                row_factory=dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! " \
                    f"Did you create it using `createdb {self.DATABASE_NAME}`?")

# redeploying our app
1. copy over files using scp
   scp -r -i ~/.ssh/cherrybee_cloud_deployment.pem \
  *.py requirements.txt Dockerfile seeds templates static \
  ec2-user@3.8.167.155:~/cherrybee_book_store
2. ssh into your EC2 instance
   ssh -i ~/.ssh/cherrybee_cloud_deployment.pem ec2-user@3.8.167.155
3. build a new image of your app
   make sure your docker is running
   make sure you cd cherrybee_book_store
   docker build -t cherrybee_book_store .
   docker images
4. stop the running cherrybee_book_store container. get id first (docker ps)
   docker stop f2ad8eb81abf (stopping the container)
5. the web page was not working (SPEAK TO COACH)

#-------------------------------------------------------------------------------
# SECURITY - SQL Injection

# Risk
1. A user writes some SQL in one of your form fields
2. That text (SQL) is then inserted (injected) into an SQL query by DatabaseConnection
3. user SQL executed
4. From our BookRepository Class
       def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)',
            [book.title, book.author]
        )
        return None
5. lets stop using params and insert user input directly, becomes the below
      def create(self, book):
        self._connection.execute(
            f"INSERT INTO books (title, author) VALUES ('{book.title}', '{book.author}')",
            []
        )
6. Now psycopg will treat the whole query as SQL and try to execute it bypassing security measures totally.

# Attacks
# 4 attacks targetting the title

# Attack 1: add a new book
1. by sticking the below line in the title field of the browser form
   legit title', 'legit author'); INSERT INTO books (title, author) VALUES ('injected title', 'injected author') --

# Attack 2: creat a new table
1. the below will create a new table, place in title field
   new title', 'new author'); CREATE TABLE target (id INT); --

# Attack 3: Delete (DROP) a table
1. Use the below
   another new title', 'another new author'); DROP TABLE target; --

# Attack 4: break your app
2. Use the below
  a newer title', 'a newer author'); DROP TABLE books; --

#----------------------------------------------------------------------------------
# HTTP Recap
# making more POST and GET requests
# POST req used to create entries in a DB, so far we have used them to create rows in our book store
# We have only seen JSON and Form data 

# FLASK and HTML - REGISTRATION
# implementing registration when a user signs up for the app
1. A users table: users: username & password & id
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

2. A User class: username & password
class User:
  def __init__(self, username, password, id = None):
    self.id = id
    self.username = username
    self.password = password

3. A UserRepository class: save method
class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Create a new user

    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            [user.username, user.password]
        )
        return None

4. A new form: signup_form.html, username, password & submit
<form action="/users" method="POST">
  <input type="text" name="username" placeholder="username" required>
  <input type="password" name="password" placeholder="password" required>

  <button type="submit">Sign Up</button>
</form>

5. A new route for serving the form: GET/users/new route, render
@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

6. Handling submission of the sign-up form
# some new imports are needed at the top of app.py
from user import User
from user_repository import UserRepository

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

#--------------------------------------------------------------------------------
# TESTING Registration

# Integration Testing: to make sure classes work together as intended
1. touch tests/test_create_user.py
2. put the below code in it

# test_create_user.py

import sys
import os

from app import app
from database_connection import DatabaseConnection

def test_create_user_is_saved_to_database():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()

    # use execute to send a TRUNCATE TABLE query 

    connection.execute("TRUNCATE TABLE users;")


   # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'

#----------------------------------------------------------------------------------
# CONTINUOUS DEPLOYMENT (CD)

# before CD, we need GitHub Actions: allows automation workflows on GitHub
1. listen for changes on the main brance
2. runs a deployment script when changes are detected

# GitHub Actions

# STEP 1: create & configure a GitHub Repo
1. create gitHub repo (any name on GitHub) - cherrybee_continuous_deployment
2. grab the remote link fro github
https://github.com/kunle-fagbenro/cherrybee_continuous_deployment.git
3. now add your remote (git init first if not git initiated)
git remote add origin <your_remote>
git remote add origin https://github.com/kunle-fagbenro/cherrybee_continuous_deployment.git
4. git remote -v
5. confirmed it worked with fetch and push displayed

# STEP 2: Configure your GitHub environment
1. settings > Environments
2. click New Environment
3. Enter prod as environment name
4. click Configure environment to confirm
5. click Add environment secret
6. Enter POSTGRES_USER as the name and postgres as the value
7. Click Add secret to confirm
8. Repeat with the appropriate values for POSTGRES_PASSWORD and EC2_HOST (your EC2 public IPv4 address)

# STEP 3: Set up SSH Access for GitHub Actions
1. run the command below to copy your SSH Key to clipboard
cat ~/.ssh/ola_cloud_deployment.pem | pbcopy
2. Add this as secret key. name = EC2_SSH_KEY and pass clipboard

# STEP 4: Create the GitHub Action Workflow
1. create a new dir called .github, subdirectory called workflows and then a file called deploy.yml
2. paste code provide (see code in /.github/workflow/deploy.yml)
