from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return f"<h1>Welcome, {username}!</h1>"
    else:
        flash("Invalid username or password")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
