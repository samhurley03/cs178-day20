from flask import Flask
import os
import socket
import random

app = Flask(__name__)

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "There are 10 types of people in the world: those who understand binary and those who dont.",
    "I would tell you a UDP joke, but you might not get it."
]

@app.route("/")
def hello():
    hostname = socket.gethostname()
    name = os.getenv("NAME", "CS178 Student")

    html = f"""
    <html>
        <head>
            <title>Sam's Friendly Flask App</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding-top: 40px;">
            <h1>👋 Welcome, {name}!</h1>
            <h3>This app is running inside Docker 🚀</h3>
            <p><b>Hostname:</b> {hostname}</p>

            <h2>💡 Random Programming Joke</h2>
            <p><i>{random.choice(jokes)}</i></p>

            <h2>🐳 Docker + Flask = Powerful Combo</h2>
            <img src="https://miro.medium.com/max/1400/1*4X5n6WfR9YH9xZlKXzJpHg.png" width="400">

            <p style="margin-top:40px;">Built with Flask & Docker</p>
        </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)