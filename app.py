from flask import Flask, render_template_string
import os
app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r') as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)