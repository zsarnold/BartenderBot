from flask import Flask     #load flask module into python script
app = Flask(__name__)       #create flask opject called app

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
