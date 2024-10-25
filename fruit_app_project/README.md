# Fruitipedia Web App

## Overview:
Fruitipedia is a web application designed for managing a collection of fruits, allowing users to add, view, edit, and delete fruits from the database. The application features a user-friendly interface for managing fruit details, including name, category, description, and nutrition information. The app is built using Python with the Django web framework, and PostgreSQL as the database.

## Features:
Fruit Management:

- Create Fruits: Users can add new fruits to the system by entering relevant details such as the fruit name, category, description, nutrition information, and an image URL.

- View Fruits: Users can view the details of all fruits available in the system, including an image, name, category, description, and nutritional value.

- Edit Fruits: Users can modify the details of an existing fruit.

- Delete Fruits: Users can delete a fruit from the system.

User Interface:

- The application provides a simple and clean user interface, styled using CSS, for easy navigation. Users can interact with the fruit management features through forms and action buttons (e.g., Edit, Delete).

- The interface includes a dashboard that displays the fruits as cards with images and brief details, allowing users to quickly browse through the collection.

Secure Form Submission:

- All forms in the application include CSRF protection, ensuring secure submission of user input. The forms are managed through Django Forms, which handle validation and rendering.

## Technologies Used:
- Python: Core programming language for the backend logic.

- Django: The web framework used to build the application, manage URL routing, and handle backend logic for CRUD operations.

- PostgreSQL: The relational database used to store fruit details.

- HTML/CSS: For designing and styling the user interface. CSS handles the layout of the fruit cards and form designs.

- Django Templates: Used to dynamically render HTML content with the data retrieved from the database.

- Django Forms: Simplifies form handling and validation during fruit creation and editing.
