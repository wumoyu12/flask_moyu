from flask import Flask

app=Flask(__name__)

@app.route("/")

def main():
    return home()
    return user()

def home():
    print("Hello I am coming to you from the Python Shell")
    return "Hello I am coming to you from the Web Page"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()
