import tkinter as tk
import datetime
import os

FILE_NAME = "reminders.txt"

# Load reminders from file
def load_reminders():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    return []

# Save reminder to file
def save_reminder(reminder):
    with open(FILE_NAME, "a") as file:
        file.write(reminder + "\n")

reminders = load_reminders()

# Clear chat
def clear_chat():
    chat.delete("1.0", "end")

# Response function
def respond():
    user_input = entry.get().lower()

    if user_input == "bye":
        chat.insert(tk.END, "Assistant: Goodbye!\n")
        window.destroy()

    elif user_input in ["hi", "hello"]:
        chat.insert(tk.END, "Assistant: Hello! How can I help you?\n")

    elif "how are you" in user_input:
        chat.insert(tk.END, "Assistant: I'm doing great!\n")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        chat.insert(tk.END, "Assistant: Current time is " + current_time + "\n")

    elif user_input.startswith("add"):
        reminder = user_input.replace("add", "").strip()
        reminders.append(reminder)
        save_reminder(reminder)
        chat.insert(tk.END, "Assistant: Reminder saved!\n")

    elif "show reminders" in user_input:
        if reminders:
            chat.insert(tk.END, "Assistant: Your reminders are:\n")
            for r in reminders:
                chat.insert(tk.END, "- " + r)
        else:
            chat.insert(tk.END, "Assistant: No reminders yet.\n")

    else:
        chat.insert(tk.END, "Assistant: Sorry, I didn't understand that.\n")

    entry.delete(0, tk.END)

# Create window
window = tk.Tk()
window.title("AI Virtual Assistant")

# FULL SCREEN
window.state("zoomed")

# ---------- CENTER FRAME ----------
center_frame = tk.Frame(window)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Chat box
chat = tk.Text(center_frame, height=20, width=60)
chat.pack(pady=10)

# Input box
entry = tk.Entry(center_frame, width=50)
entry.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(center_frame)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Send", command=respond)
send_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear Chat", command=clear_chat)
clear_button.pack(side="left", padx=5)

window.mainloop()