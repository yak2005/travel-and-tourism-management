from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session and flash messages

# Dummy user data for testing (replace with a database in production)
users = {'testuser': 'password'}

# Home Page (requires login)
@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

# Destinations Page (requires login)
@app.route('/destinations')
def destinations():
    if 'username' not in session:
        return redirect(url_for('login'))
    destinations = [
        {'name': 'Paris', 'description': 'City of Light', 'price': 2000},
        {'name': 'London', 'description': 'Historic Charm', 'price': 1800},
        {'name': 'Tokyo', 'description': 'Land of the Rising Sun', 'price': 3000},
        {'name': 'Dubai', 'description': 'City of Gold', 'price': 2800},
        {'name': 'Sydney', 'description': 'The Harbour City', 'price': 2600},
        {'name': 'Rome', 'description': 'Eternal City', 'price': 2200},
        {'name': 'Bangkok', 'description': 'City of Angels', 'price': 1500},
        {'name': 'Cape Town', 'description': 'Mother City', 'price': 2400},
        {'name': 'Rio de Janeiro', 'description': 'Marvelous City', 'price': 2700},
    ]
    return render_template('destinations.html', destinations=destinations)

# Booking Page (requires login)
@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        destination = request.form['destination']
        flash('Booking Successful! Thank you, {}.'.format(name))
        return redirect(url_for('book'))
    destinations = ['Paris', 'London', 'New York']
    return render_template('booking.html', destinations=destinations)

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists. Please login.')
            return redirect(url_for('login'))
        users[username] = password
        flash('Signup Successful! Please login.')
        return redirect(url_for('login'))
    return render_template('signup.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login Successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
