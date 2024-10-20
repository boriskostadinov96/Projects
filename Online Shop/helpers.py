from hashlib import sha256

from canvas import frame


def clean_screen():
    frame.delete("all")


def password_secured(password):
    hash_object = sha256(password.encode())
    return hash_object.hexdigest()