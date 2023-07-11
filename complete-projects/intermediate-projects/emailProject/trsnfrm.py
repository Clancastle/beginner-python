from flask import Flask, request, render_template

"first save the data to a file, and cookies"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    age = request.form.get('age')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    return "thanks for signing up!"
if __name__ == "__main__":
    app.run()