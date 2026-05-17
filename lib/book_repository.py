from lib.book import Book

class BookRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # # Retrieve all books
    # def all(self):
    #     rows = self._connection.execute('SELECT * from books')
    #     books = []
    #     for row in rows:
    #         item = Book(row["id"], row["title"], row["author"])
    #         books.append(item)
    #     return books
    
    #COMMENTED THE ALL METHOD ABOVE TO PAVE WAY FOR POST REQUEST BELOW
    #----------------------------------------------------------------
    # id is now the third argument
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["title"], row["author"], row["id"])
            books.append(item)
        return books


    #------------------------------------------------------------------
    # note that my BookRepository works with instances of Book
    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author) VALUES (%s, %s)',
            [book.title, book.author]
        )
        return None
    




    # # Find a single book by their id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author"])

    # # Create a new book
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, book):
    #     self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', [
    #     book.title, book.author])
    #     return None

    # # Delete an book by their id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM artists WHERE id = %s', [book_id])
    #     return None