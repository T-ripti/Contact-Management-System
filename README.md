# Contact-Management-System

# Overview
This project is a simple GUI application built using Python and PyQt5. The application includes a main window with a single button. When the button is clicked, a message is printed to the console. Additionally, the project includes a SQLite database (Contectfile.db) to manage contact information.

# Features
Graphical User Interface (GUI): The main window includes a button that triggers a console message when clicked.
SQLite Database Integration: The application connects to an SQLite database to manage contact information.

# File Structure
main.py: The entry point of the application. It initializes and starts the PyQt5 application.
gui.py: Defines the main window and its components, including the button and its click event.
Contectfile.db: An SQLite database file containing a contacts table to store contact information.

# Requirements
Python 3.x
PyQt5

# Installation
1. Clone the repository:
   git clone https://github.com/T-ripti/Contact-Management-System.git
3. Navigate to the project directory:
   cd Contact-Management-System
5. Install the required packages:
   pip install PyQt5

# Usage
Run the application: python main.py
Interacting with the GUI: Click the "Click me!" button to trigger a console message.

# Database
The application uses an SQLite database (Contectfile.db) to manage contact information. The database contains a single table named contacts with the following schema:
id: INTEGER, Primary Key, Auto Increment
name: TEXT
email: TEXT
phone: INTEGER
