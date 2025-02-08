## pip install flask
from flask import Flask   ### import Flask class from flask module

app = Flask(__name__)  ### create an instance of Flask class
### Dont make any changes to the above code


@app.route('/')  ### decorator
def index():
    return "<h1> Hello Guys from We4AI! </h1> <h2> Welcome to the world of AI </h2>"


### DONT Change the code below
if __name__ == '__main__':
    app.run(debug=True)  ### run the app

