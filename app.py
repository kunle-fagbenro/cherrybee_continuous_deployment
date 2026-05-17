# from flask import Flask, render_template #1

# # Minimal Flask App
# #---------------------------------------------------------------------------------
# # instantiate a Flask app object
# app = Flask(__name__) #1
# #--------------------------------------- #2 
# #route that listens for a get
# @app.route('/hello', methods=['GET']) #2
# def hello(): #2
#     return "Hello to you too" #2
# #----------------------------------------#2
# # ----------------------------------------------#3
# #3 duplicate route
# @app.route('/hello', methods=['GET']) #3
# def hello_again(): #3
#     return "Hello, hello and hello again!" #3
# #-----------------------------------------------#3
# #------------------------------------------------------------#4
# # create new route that responds to requests sent with method GET and PATH /books
# @app.route('/books', methods=['GET']) #4
# def get_books(): #4
#     return [
#   {
#     "title": "The Gruffalo",
#     "author": "Julia Donaldson"
#   },
#   {
#     "title": "Ada Twist, Scientist",
#     "author": "Andrea Beaty"
#   },
#   {
#     "title": "The Girl Who Drank the Moon",
#     "author": "Kelly Barnhill"
#   },
#   {
#     "title": "Dragons in a Bag",
#     "author": "Zetta Elliott"
#   }
# ] #4

# #--------------------------------------------------------------------#5
# # Challenge route for GET/authors
# @app.route('/authors', methods=['GET'])
# def authors():
#     return [
#   {
#     "name": "Julia Donaldson",
#     "dob": "1948-09-16"
#   },
#   {
#     "name": "Andrea Beaty",
#     "dob": "1961-10-08"
#   },
#   {
#     "name": "Kelly Barnhill",
#     "dob": "1973-01-01"
#   },
#   {
#     "name": "Zetta Elliott",
#     "dob": "1979-11-11"
#   }
# ]
# #---------------------------------------------------------------------#5
# #----------------------------------------------------------------------#6
# # PAIR PROGRAMMING 1
# @app.route('/quotes', methods=['GET'])
# def quotes():
#     return [
#   {
#     "name": "Julia Donaldson",
#     "quote": "I love writing stories that children can join in with."
#   },
#   {
#     "name": "Andrea Beaty",
#     "quote": "Curiosity is the spark that drives discovery."
#   },
#   {
#     "name": "Kelly Barnhill",
#     "quote": "Stories are the way we make sense of the world."
#   },
#   {
#     "name": "Zetta Elliott",
#     "quote": "Books can be both mirrors and windows."
#   }
# ]
# #=====================================================================#7
# # route for index GET /
# @app.route("/", methods=['GET'])
# def index():
#     return render_template("index.html")

# #======================================================================#8
# # route for books.html
# @app.route("/books.html", methods=['GET'])
# def books_render():
#     return render_template("books.html")

# #=======================================================================#9
# @app.route("/change.html", methods=['GET'])
# def change_render():
#     return render_template("change.html")


# #--------------------------------------------------------------#1
# # make the server run in response to `python app.py`
# # on port 5001 (you'll learn more about what this means later)
# # and use debug mode so that changing code restarts the app
# if __name__ == "__main__":  #1
#     app.run(host="0.0.0.0", port=5001, debug=True) #1
#----------------------------------------------------------------------------------

# I HAVE COMMENTED OUT ALL THE ABOVE TO CONCENTRATE NOW ON THE READING FROM THE DATABASE

from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user import User
from lib.user_repository import UserRepository

app = Flask(__name__)
#-----------------------------------------------------------------
@app.route('/books', methods=['GET'])
def get_all_books():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  print(books)
  return render_template("books.html", books=books)
#--------------------------------------------------------------------
# UPDATED VERSION BELOW.
# /books route so that books is passed into book.html template

# @app.route('/books', methods=['GET'])
# def get_all_books():
#   connection = DatabaseConnection()
#   connection.connect()
#   book_repository = BookRepository(connection)
#   books = book_repository.all()
#   return render_template("books.html", books=books)

#------------------------------------------------------------------------
# Jinja Templates 

# @app.route('/team', methods=['GET'])
# def get_team():
#     team = ["Dorothy", "Rose", "Blanche", "Sophia"]
#     return render_template("team.html", team=team)

#------------------------------------------------------------------------
# this route created to be used used with curl in your terminal
# to handle POST and grab request body
# but does notnyet create new books in database 

# @app.route('/books', methods=['POST'])
# def create_book():
#   book_details = request.json
#   print(book_details)
#   return "created", 201

#------------------------------------------------------------------------
# UPDATED POST ROUTE BELOW

# @app.route('/books', methods=['POST'])
# def create_book():
#     # make a new database connection
#     connection = DatabaseConnection()
#     connection.connect()

#     # make a new instance of BookRepository
#     book_repository = BookRepository(connection)

#     # get the request body
#     # book_details = request.json

#     # request body now changed to HTML FORM data (updating the POST route)
#     book_details = request.form

#     # my BookRepository expects an instance of Book, so make one here
#     book = Book(title=book_details["title"], author=book_details["author"])

#     # save the book
#     book_repository.create(book)

#     # return a 201, which means "created"
#     return "created", 201
      # COMMENTED THE ABOVE FOR THE BELOW
#-------------------------------------------------------------------------
# UPDATED POST ROUTE BELOW WITH RENDERING THE REQUEST FORM

# @app.route('/books', methods=['POST'])
# def create_book():
#     connection = DatabaseConnection()
#     connection.connect()
#     book_repository = BookRepository(connection)
#     book_details = request.form
#     book = Book(title=book_details["title"], author=book_details["author"])
#     book_repository.create(book)
#     books = book_repository.all()  
#     return render_template("books.html", books=books)
# COMMENTED THE ABOVE OUT TO SUIT THE REDIRECTION BELOW
#--------------------------------------------------------------------------
# REDIRECTION DONE PROPERLY BELOW LET USER MAKE ANOTHER GET REQUEST 

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")


@app.route('/users/new', methods=['GET'])
def get_signup_form():
  
  return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("books")

#-------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    