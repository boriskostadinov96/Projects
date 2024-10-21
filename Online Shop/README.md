# Online Shopping Application

## Overview:
This is a simple Online Shopping Application built with Python using the Tkinter library for the graphical user interface (GUI). The application allows users to register, log in, view available products, and purchase items.

## Features:
User Registration & Login:

New users can register with their first name, last name, username, and password.
Registered users can log in securely with hashed passwords using SHA-256.
Product Display:

Displays a list of available products with images, stock availability, and a "Buy" button.
Products are dynamically loaded from a JSON file (products.json).
Product Purchasing:

Users can purchase available products, and the stock is updated in real-time.
The stock and product details are managed through a JSON file.

## Technologies Used:
Python

Tkinter: For building the GUI (buttons, text fields, images, etc.).

Pillow (PIL): For handling and displaying images within the application.

JSON: To store product information and user data.

Hashlib: For secure password hashing using SHA-256.

## File Structure:
main.py: Entry point of the application, displaying the home page.
authentication.py: Handles user registration, login, and validation.
buying_page.py: Displays available products and manages the buying functionality.
canvas.py: Initializes the Tkinter window and canvas for displaying widgets.
helpers.py: Contains utility functions like screen cleaning and password hashing.
db/products.json: Stores product data (name, stock quantity, image path).
db/users_info.txt: Stores registered user information in JSON format.
