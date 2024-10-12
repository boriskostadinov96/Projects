import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()  # download the image

    image_stream = BytesIO(image_data)  # save the image in the RAM memory

    image = ImageTk.PhotoImage(Image.open(image_stream))  # we are parsing the image into a tkinter object

    image_label.config(image=image)
    image_label.image = image # keeps reference to the image so it won't be deleted by the garbage collector


def get_image_url() -> str:
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDJlOGI0YjgtZTczYS00YmI0LWFhMWUtNDlmZmZiYjhhMmMxIiwidHlwZSI6ImFwaV90b2tlbiJ9.5z2AaI2G8TjnqZfNUbHe7tEg0WhumNQ5Ug8S3JJ9gQM"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['items'][0]["image_resource_url"]


def generate_image():
    print("button is clicked")

    try:
        error_label.place_forget()  # it will delete the error message, when we have a valid message
        image_url = get_image_url()

    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("Image Generator")
window.geometry("500x350")

error_label = tk.Label(window, text="Please enter text here", fg="red")

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

image_label = tk.Label(window)  # displaying the image in the window
image_label.place(x= 125, y=70)

generate_button = tk.Button(window, text="Generate", height=1, command=generate_image)
generate_button.place(x=300, y=16)

window.mainloop()