# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("http://127.0.0.1:5001")

#     h1 = page.locator("h1")

#     expect(h1).to_have_text("Welcome to AceReads")

# def test_has_title_in_books_html(page: Page):
#     page.goto("http://127.0.0.1:5001/books.html")

#     h1 = page.locator("h1")

#     expect(h1).to_have_text("Children's Book Collection")

# # def test_book_list_contains_all_books(page: Page):
# #     page.goto("http://127.0.0.1:5001/books")

# #     books = page.locator('li')

# #     expected_books = [
# #       'The Gruffalo by Julia Donaldson',
# #       'Ada Twist, Scientist by Andrea Beaty',
# #       'The Girl Who Drank the Moon by Kelly Barnhill',
# #       'Dragons in a Bag by Zetta Elliott'
# #     ]

# #     # here's the neat part which saves you from iterating over the `li` elements
# #     actual_books = books.all_inner_texts()

# #     assert actual_books == expected_books

# COMMENTED OUT THE ABOVE TO RUN NEW PLAYWRITE TEST WITH HTML FORM

#==============================================================================
# BELOW IS TESTING HTML FORM. 2 FIELDS AND A SUBMIT BUTTON
# in a new file called `test_create_new_book.py`

from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection
import os

def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    # the rest is unchanged
