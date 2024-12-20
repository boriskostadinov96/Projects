# Projects:

# 1.Music Web Application 
## <a href="https://github.com/boriskostadinov96/Music-App">Link to repository</a>

## Overview:
This is a music web application built with Python using Django as the web framework, SQLAlchemy for ORM, and PostgreSQL as the database. The application allows users to manage music albums and songs, providing functionalities for creating, editing, deleting, and viewing albums and songs.

## Features:
Album Management:

- Users can create, view, edit, and delete music albums. Each album has a name, an image URL, and a price.

Song Management:

- Users can add songs to albums. Each song includes a name and a music file, which can be uploaded directly through the application.

Music Playback:

- Users can play songs directly within the application. Songs are served from the database, allowing for seamless playback.

User Interface:

- The application features a user-friendly web interface built with Django templates, allowing for easy navigation between album and song management.

## Features:
Add/Set Items:

- Uses a custom hash function to map keys to indices.

Resizing:

- Automatically expands storage when needed.

Sort:

- Returns a new, sorted hash table by keys in ascending order.

- String Representation: Outputs a readable version of stored items.

- Automatically expands storage when needed.
## Technologies Used:
- Python: The core programming language for the application.

- Django: The web framework used for developing the application.

- SQLAlchemy: An ORM used for database interaction and management.

- PostgreSQL: The database system used to store album and song information.

- HTML/CSS: For designing the user interface and styling the application.

- Django Forms: For handling user input and validation during album and song creation.


# 2.AI Image Generator
## <a href="https://github.com/boriskostadinov96/AI-Image-Generator">Link to repository</a>

## Overview:
This Image Generator Application allows users to generate images based on a text prompt using an API. The application sends the text to a third-party image generation service, retrieves the image, and displays it within the GUI. It's built using Python with the Tkinter library for the graphical user interface (GUI) and integrates the EdenAI API for image generation.

# Features:
- Text-to-Image Generation:
Users can input a text description, which is sent to the EdenAI API.
The API returns a generated image based on the provided text, which is then displayed in the application.

- Error Handling:
Displays an error message if the user input is invalid or no image can be generated.

# Technologies Used:
- Python

- Tkinter: For building the GUI (buttons, text fields, image display).

- Pillow (PIL): For handling and displaying images within the application.

- Requests: For making API requests to the EdenAI API.

- EdenAI API: Provides the image generation service based on text input.

# How It Works:
- User enters a text prompt in the input field.

- On clicking the "Generate" button, the text is sent to the EdenAI API, which generates an image.

- The image is then displayed within the application's window.

# API Setup

To use this project, you need an API key from EdenAI to access their image generation services. You can set your API key in the get_image_url() function's header section.


# 3.Fruitipedia Web App
## <a href="https://github.com/boriskostadinov96/Fruitipedia">Link to repository</a>

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





# 4.Online Shopping Application
## <a href="https://github.com/boriskostadinov96/Online-Shop-Application">Link to repository</a>

## Overview:
This is a simple Online Shopping Application built with Python using the Tkinter library for the graphical user interface (GUI). The application allows users to register, log in, view available products, and purchase items.

## Features:
User Registration & Login:

- New users can register with their first name, last name, username, and password.
- Registered users can log in securely with hashed passwords using SHA-256.

Product Display:

- Displays a list of available products with images, stock availability, and a "Buy" button.
- Products are dynamically loaded from a JSON file (products.json).

Product Purchasing:

- Users can purchase available products, and the stock is updated in real-time.
- The stock and product details are managed through a JSON file.

## Technologies Used:
- Python

- Tkinter: For building the GUI (buttons, text fields, images, etc.).

- Pillow (PIL): For handling and displaying images within the application.

- JSON: To store product information and user data.

- Hashlib: For secure password hashing using SHA-256.

## File Structure:
- main.py: Entry point of the application, displaying the home page.

- authentication.py: Handles user registration, login, and validation.

- buying_page.py: Displays available products and manages the buying functionality.

- canvas.py: Initializes the Tkinter window and canvas for displaying widgets.

- helpers.py: Contains utility functions like screen cleaning and password hashing.

- db/products.json: Stores product data (name, stock quantity, image path).

- db/users_info.txt: Stores registered user information in JSON format.


# 5.Phonebook Web Application
## <a href="https://github.com/boriskostadinov96/Phonebook-Web-App">Link to repository</a>

## Overview:
This is a phonebook web application built with Python using Django as the web framework and SQLite3 as the database. The application allows users to manage contacts, providing functionalities for creating and viewing stored contacts in a simple interface.

## Features:
Contact Management:

- Users can add new contacts to the phonebook. Each contact has a name and a phone number, which are entered through a web form.

Contact List Display:

- All saved contacts are displayed on the main page, providing a quick overview of stored contact details in a simple table format.

User Interface:

- The application features a straightforward, user-friendly interface built with Django templates. It includes navigation and form handling, making it easy to add and view contacts.

## Technologies Used:
- Python: The core programming language for the application.

- Django: The web framework used for developing the application.

- SQLite3: Database system used to store and retrieve contact information.

- HTML/CSS: For structuring and styling the user interface.

- Django Templates: For rendering dynamic content, including contact lists and form handling for adding contacts.


# 6.Custom Hash Table Project
## <a href="https://github.com/boriskostadinov96/Projects/tree/main/custom_hash_table">Link to repository</a>

## Overview:
This project implements a custom hash table in Python, similar to a dictionary, with added features like automatic resizing, sorting, and error handling. The project includes unit tests to ensure correct functionality.

## Features:
Key-Value Storage:

- Stores unique key-value pairs, updating values for existing keys.

Automatic Resizing:

- Doubles capacity when full.

Sorting:

- Supports sorting by keys or values (ascending/descending; pending implementation).

Error Handling:

- Raises KeyError for missing keys.

## Technologies Used:
- Python

- Unit Testing:

# 7.Custom List
## <a href="https://github.com/boriskostadinov96/Projects/tree/main/custom_list_project">Link to repository</a>

## Overview:
This project is a custom list implementation in Python, designed to mimic Python's built-in list but with added functionality such as dynamic resizing, sorting options, and robust error handling. The project includes unit tests to verify functionality.

## Features:
Dynamic List Storage:

- Stores elements with the capability to expand capacity as needed.

Automatic Resizing:

- Automatically expands the list's capacity when it reaches a set threshold.

Sorting:

- Supports sorting elements in ascending or descending order (still in development).

Error Handling:

- Raises appropriate exceptions (e.g., IndexError) for invalid operations, such as accessing elements out of range.

## Technologies Used:
- Python: Used for the core list functionality

- Unit Testing: : Tests are included to validate correct behavior of the list methods and error handling.
