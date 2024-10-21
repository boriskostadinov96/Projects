# Image Generator Application

## Overview:
This Image Generator Application allows users to generate images based on a text prompt using an API. The application sends the text to a third-party image generation service, retrieves the image, and displays it within the GUI. It's built using Python with the Tkinter library for the graphical user interface (GUI) and integrates the EdenAI API for image generation.

# Features:
Text-to-Image Generation:
Users can input a text description, which is sent to the EdenAI API.
The API returns a generated image based on the provided text, which is then displayed in the application.

Error Handling:
Displays an error message if the user input is invalid or no image can be generated.

# Technologies Used:
Python:

Tkinter: For building the GUI (buttons, text fields, image display).

Pillow (PIL): For handling and displaying images within the application.

Requests: For making API requests to the EdenAI API.

EdenAI API: Provides the image generation service based on text input.

# How It Works:
User enters a text prompt in the input field.

On clicking the "Generate" button, the text is sent to the EdenAI API, which generates an image.

The image is then displayed within the application's window.

API Setup

To use this project, you need an API key from EdenAI to access their image generation services. You can set your API key in the get_image_url() function's header section.
