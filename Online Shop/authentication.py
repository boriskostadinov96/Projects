from tkinter import Button
from canvas import window, frame


def home_page():
    register_button = Button(
        window,
        text="Register",
        bg="green",  # background color
        fg="white",  # font color
        bd=0,  # without frame / border
        width=10,
        height=1,
        command=register
    )

    login_button = Button(
        window,
        text="Login",
        bg="orange",
        fg="white",
        bd=0,
        width=10,
        height=1,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 290, window=login_button)


def register():
    print("Registered")


def login():
    print("Logged")
