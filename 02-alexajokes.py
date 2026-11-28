
import tkinter as tk
from tkinter import messagebox
import random
import pyttsx3


# ------------------------
# Initialize Alexa Voice Engine
# ------------------------
alexa = pyttsx3.init()
alexa.setProperty("volume", 1.0)


# ------------------------
# Make Alexa Speak
# ------------------------
def speak(text):
    print("Alexa:", text)
    alexa.say(text)
    alexa.runAndWait()


# ------------------------
# Built-in Joke List
# ------------------------
jokes = [
    ("Why did the computer go to the doctor?",
     "Because it had a virus!"),

    ("Why was the math book sad?",
     "Because it had too many problems!"),

    ("What do you call a bear with no teeth?",
     "A gummy bear!"),

    ("Why did the student eat his homework?",
     "Because the teacher said it was a piece of cake!"),

    ("Why can't your nose be 12 inches long?",
     "Because then it would be a foot!"),

    ("What do you call a fish wearing a bowtie?",
     "Sofishticated!"),

    ("Why did the bicycle fall over?",
     "Because it was two-tired!"),

    ("What did one wall say to the other wall?",
     "I'll meet you at the corner!"),

    ("Why did the cookie go to the hospital?",
     "Because it felt crummy!"),

    ("What do you call a sleeping dinosaur?",
     "A dino-snore!")
]


# ------------------------
# Tell a Joke
# ------------------------
def tell_joke():
    global current_setup, current_punchline

    current_setup, current_punchline = random.choice(jokes)

    setup_label.config(text=current_setup)
    punchline_label.config(text="")

    speak(current_setup)


# ------------------------
# Show Punchline
# ------------------------
def show_punchline():
    if current_punchline:
        punchline_label.config(text=current_punchline)
        speak(current_punchline)

    else:
        messagebox.showinfo(
            "No Joke",
            "Please select a joke first!"
        )


# ------------------------
# Next Joke
# ------------------------
def next_joke():
    tell_joke()


# ------------------------
# Quit Program
# ------------------------
def quit_program():
    speak("Goodbye. Have a wonderful day.")
    root.destroy()


# ------------------------
# Create Main Window
# ------------------------
root = tk.Tk()
root.title("Alexa Joke Assistant")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="lightblue")


# ------------------------
# Variables
# ------------------------
current_setup = ""
current_punchline = ""


# ------------------------
# Heading
# ------------------------
title_label = tk.Label(
    root,
    text="Alexa Joke Assistant",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)


# ------------------------
# Joke Setup Label
# ------------------------
setup_label = tk.Label(
    root,
    text="Click the button and Alexa will tell you a joke!",
    font=("Arial", 12),
    wraplength=500,
    bg="white",
    width=60,
    height=4
)
setup_label.pack(pady=10)


# ------------------------
# Punchline Label
# ------------------------
punchline_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "italic"),
    fg="blue",
    bg="lightblue",
    wraplength=500
)
punchline_label.pack(pady=10)


# ------------------------
# Buttons
# ------------------------
btn_joke = tk.Button(
    root,
    text="Alexa Tell Me a Joke",
    command=tell_joke,
    width=20
)
btn_joke.pack(pady=5)


btn_punchline = tk.Button(
    root,
    text="Show Punchline",
    command=show_punchline,
    width=20
)
btn_punchline.pack(pady=5)


btn_next = tk.Button(
    root,
    text="Next Joke",
    command=next_joke,
    width=20
)
btn_next.pack(pady=5)


btn_quit = tk.Button(
    root,
    text="Quit",
    command=quit_program,
    bg="red",
    fg="white",
    width=20
)
btn_quit.pack(pady=10)


# ------------------------
# Welcome Message
# ------------------------
speak(
    "Hello, I am Alexa. "
    "Click the button and I will tell you a joke."
)


# ------------------------
# Start GUI
# ------------------------
root.mainloop()