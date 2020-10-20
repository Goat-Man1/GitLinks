from flask import Flask, render_template, redirect, url_for, request
app = Flask('app')


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/links')
def links():
	return render_template('links.html')


@app.route('/goatshomeoksdfgklesngiuwenoifbeoigbseoifdhbosueijhgnuokgjsdknfskdfk')
def admin():
	return render_template('admin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'goat' or request.form[
		    'password'] != 'isacim51':
			error = 'Invalid Credentials. Please try again.'

		else:
			return redirect(url_for('admin'))
	return render_template('login.html', error=error)


app.run(host='0.0.0.0', port=8080)