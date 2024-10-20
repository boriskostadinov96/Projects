from tkinter import Tk, Canvas


def create_window():
    window = Tk()

    window.title("Online Shop")
    window.geometry("700x600")
    window.resizable(False, False)

    return window


def create_frame():
    frame = Canvas(window, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


window = create_window()
frame = create_frame()