from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<h2>Here is an interesting golf course picture for you: </h2>" \
           '<img src="https://www.top100golfcourses.com/_next/image?url=https:%2F%2Fcdn.sanity.io%2Fimages%2F03mhssoh%2Fproduction%2F282ce428f9af676a8104f24dfa4219969d356a5f-2400x1404.jpg&w=1920&q=75">'
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)