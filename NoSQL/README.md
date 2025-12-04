NoSQL – MongoDB Project

This project introduces the fundamentals of NoSQL databases, with a focus on MongoDB and its interaction both through the Mongo shell and Python using PyMongo.

It covers document storage, basic CRUD operations, filtering, counting, updating, deleting, and performing simple analytics with MongoDB.

📚 Learning Objectives

By the end of this project, you should be able to explain without external help:

► General NoSQL Knowledge

What NoSQL means

Differences between SQL and NoSQL

What ACID means

What document storage is

The different types of NoSQL databases

Benefits of NoSQL databases

► MongoDB Operations

How to query MongoDB

How to insert, update, and delete documents

How to use the mongo shell

How to use MongoDB with Python via PyMongo

🛠 Requirements
✔ MongoDB Command Files (Tasks 0–7)

Interpreted on Ubuntu 20.04 LTS, MongoDB 4.4

The first line must be:

// my comment


Files must end with a newline

Code length checked using wc

✔ Python Scripts (Tasks 8–12)

Executed with Python 3.9 and PyMongo 4.8.0

The first line must be:

#!/usr/bin/env python3


Must follow pycodestyle 2.5*

All modules and functions must have documentation

Must not execute on import (use:

if __name__ == "__main__":


)

✔ README.md

A README is required at the root of the project (this file).

🗂 List of Tasks
0. List all databases

Write a script that prints all MongoDB databases.

1. Create or use a database

Script that switches to or creates the database my_db.

2. Insert a document

Insert { name: "Holberton school" } into the school collection.

3. List all documents

Display all documents inside the collection school.

4. List all matches

List documents where name="Holberton school".

5. Count documents

Count all documents in the school collection.

6. Update documents

Update all documents with name="Holberton school" to add:

{ "address": "972 Mission street" }

7. Delete documents

Delete all documents with name="Holberton school".

🐍 Python Tasks
8. List all

Function that lists all documents in a collection.

9. Insert with kwargs

Insert a new document and return the _id.

10. Update topics

Update the topics list of a given school.

11. Schools by topic

Return all schools containing a specific topic.

12. Log statistics

Read logs stored in MongoDB and display:

total log count

count for each HTTP method

count of GET requests to /status

🧪 Example Commands
Run a MongoDB script:
cat 0-list_databases | mongo

Run a Python task:
./8-main.py

Restore the Nginx dump:
mongorestore dump

🛑 Important Notes

All files must respect the required format (first line, newline, length).

Python scripts must include proper documentation.

MongoDB queries must run without errors on MongoDB 4.4.

All tasks are tested automatically by Holberton’s checker.

👨‍💻 Author

Project from Holberton School – Web Back-End Track
NoSQL module written by Emmanuel Turlay and Guillaume Salva.