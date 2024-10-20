from tkinter import Button, Entry
from canvas import window, frame
from helpers import clean_screen, password_secured
from buying_page import display_products
import json


def get_users_data():
    info_data = []

    with open("db/users_info.txt", "r") as users_file:
        for line in users_file:
            info_data.append(json.loads(line))

    return info_data


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
    clean_screen()

    frame.create_text(100, 50, text="Firs Name:")
    frame.create_text(100, 100, text="Last Name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_field)
    frame.create_window(200, 100, window=last_name_field)
    frame.create_window(200, 150, window=username_field)
    frame.create_window(200, 200, window=password_field)

    register_button = Button(
        window,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=10,
        height=1,
        command=registration
    )

    frame.create_window(315, 250, window=register_button)


def registration():
    user_data = {
        "First name": first_name_field.get(),
        "Last name": last_name_field.get(),
        "Username": username_field.get(),
        "Password": password_field.get(),
    }

    if valid_registration(user_data):
        with open("db/users_info.txt", "a") as users_file:
            user_data["Password"] = password_secured(user_data["Password"])
            json.dump(user_data, users_file)
            users_file.write("\n")
            display_products()


def valid_registration(user_data):
    frame.delete("error")

    for key, value in user_data.items():
        if not value.strip():
            frame.create_text(
                150,
                250,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )
            return False

    user_information = get_users_data()

    for user in user_information:
        if user["Username"] == user_data["Username"]:
            frame.create_text(
                200,
                300,
                text="Username is already taken!",
                fill="red",
                tags="error",
            )

            return False

    return True


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(230, 50, window=username_field)
    frame.create_window(230, 100, window=password_field)

    frame.create_window(300, 150, window=login_button)


def logging():
    if valid_login():
        display_products()

    else:
        frame.create_text(
            200,
            200,
            text="Invalid username or password!",
            fill="red",
            tags="error",
        )


def valid_login():
    users_data = get_users_data()

    user_username = username_field.get()
    user_password = password_secured(password_field.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_field.get(),
        password_field.get(),
    ]

    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break

    else:
        login_button["state"] = "normal"


first_name_field = Entry(window, bd=0)
last_name_field = Entry(window, bd=0)
username_field = Entry(window, bd=0)
password_field = Entry(window, bd=0, show="*")

login_button = Button(
    window,
    text="Login",
    bg="orange",
    fg="white",
    bd=0,
    width=10,
    height=1,
    command=logging,
)

login_button["state"] = "disabled"

window.bind("<KeyRelease>", change_login_button_status)