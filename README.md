# Python Assignment

This repository contains code written for Module 3: Software Development Fundamentals.

The application is a Continuous Integration Health Checker, written to help users monitor automated tests running on a GitLab server.

It connects to a private GitLab instance and fetches job information from a specific group. This is used to populate the jobs csv file.

## Requirements

This application requires the `python-gitlab` module - find the docs here https://python-gitlab.readthedocs.io/en/stable/index.html.

To run this application with full GitLab functionality, the `exampleKey.py` file should be renamed to `key.py` and the placeholders replaced. 

## To Do

General:
* Error handling for files, corrupted data, inputs
* Formatting

Refactoring:
* `dataUI.py` (still quite long after first refactor)
* `jobHandling.py` (long/complicated)
* `main.py` (break each statement into methods?)

Testing (manual/automated):
* `addEntries.py`
* `dataUI.py`
* `deleteEntries.py`
* `editEntries.py`
* `inputValidation.py`
* `jobHandling.py`

## Assignment Brief

* To design, develop and test a simple console-based application in Python using a basic systems development approach with a supporting description of the programming concepts and syntax, and the systems development processes used.

* The application should include a Data Store that can be implemented as either a simple Comma Separated Value (CSV) file or a single table in an SQLite database. 

* The finished Data Store should contain 10 sample records and each record should be made up of at least 8 fields that include a range of appropriate data types. A suitable field should be included to act as the Primary Key.

* The application should start with a menu that allows the user to browse all the records in the Data Store, add a new record, or amend, delete or display the full details of a selected record.

* Validation should be included so that the user cannot perform an invalid action or enter non-conformant data for a field. Appropriate error messages should be displayed when validation rules are breached.

## Guidelines

* Your solution should adhere to the basic design guidelines of modularisation by dividing the functionality up into appropriate elements.

* Ensure the quality and readability of your code by following basic programming guidelines such as naming conventions, indentation, comments and refactoring to avoid duplication of logic.

* Usability should be considered. For example, after completing an option, the user should be shown an appropriate message that indicates the success or failure of their action. Also, to confirm with the user before quitting the application or deleting a record.

* The user should be able to return to the Main Menu no matter where they are in the application.

* When the Data Store is read into the application, there should be checks to ensure no data is corrupt. For example, all Primary Keys are unique and all data conforms to the validation rules. If the data in a returned row is found to be corrupt, an error message should be written to a log file, the row should be skipped and the rest of the file/dataset treated normally.
