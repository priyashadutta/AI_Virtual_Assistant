import datetime

def assistant():
    print("Hello! I am your Virtual Assistant.")
    print("You can ask me to set reminders, tell time, or ask simple questions.")
    print("Type 'bye' to exit.\n")

    reminders = []
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("Assistant: Goodbye! Have a great day.")
            break

        # Greeting
        elif user_input in ["hi", "hello"]:
            print("Assistant: Hello! How can I help you?")

        # How are you
        elif "how are you" in user_input:
            print("Assistant: I'm doing great! Thanks for asking.")

        # Tell time
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Assistant: Current time is", current_time)

        # Set reminder
        elif "reminder" in user_input:
            reminder = input("Enter your reminder: ")
            reminders.append(reminder)
            print("Assistant: Reminder saved!")

        # Show reminders
        elif "show reminders" in user_input:
            if reminders:
                print("Assistant: Your reminders are:")
                for r in reminders:
                    print("-", r)
            else:
                print("Assistant: No reminders yet.")

        # Unknown command
        else:
            print("Assistant: Sorry, I didn't understand that.")

assistant()