# BookStore

A RESTful API using FastAPI for an online book store that supports the ability for users to rate books. 
The application provides endpoints for CRUD operations on books and ratings.

There are two parts to this application:
1. Book-related
2. Rating-related

Book-related API endpoints:

POST /books: Adds a new book to the database.
GET /books/{id}: Retrieves the details of a specific book.
PUT /books/{id}: Updates the details of a specific book.
DELETE /books/{id}: Deletes a specific book.
GET /books: Retrieves details of all books.
GET /books/rated: Retrieves details of all books sorted by their average ratings, highest first.


Rating-related
POST /ratings: Adds a new rating for a book (a user can only rate a book once).
GET /ratings/{book_id}: Retrieves all ratings for a specific book.

I have used MySQL database and SQLAlchemyORM to interact with the database.

To the run the application,clone the repository into your personal machine and update the database name,username and password in the query:
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{username}:{password}@127.0.0.1:3306/{yourdbname}' which can be found in database.py



