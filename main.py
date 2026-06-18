from datetime import datetime

print("Rest & Reflect - Night Check-In")
print("--------------------------------")

mood = input("How do you feel tonight? ")
gratitude = input("What is one thing you are grateful for today? ")
stress = input("What is one thing weighing on your mind? ")
tomorrow = input("What is one small thing you want to do tomorrow? ")

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

entry = f"""
Date: {date}
Mood: {mood}
Gratitude: {gratitude}
Stress: {stress}
Tomorrow's Focus: {tomorrow}
--------------------------------
"""

with open("checkins.txt", "a") as file:
    file.write(entry)

print("\nYour check-in has been saved.")
print("Good job slowing down and reflecting.")
