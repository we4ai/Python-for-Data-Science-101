from flask import Flask, render_template

app = Flask(__name__)

### Dont make any changes to the above code

@app.route('/')
def index():
    return render_template('index.html')


### DONT Change the code below
if __name__ == '__main__':
    app.run(debug=True)  
