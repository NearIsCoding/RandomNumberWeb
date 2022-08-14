from itertools import permutations
from sys import stdout
from flask import Flask, render_template, request, make_response, redirect, url_for

from random_variable import generate

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')



# Creating different routes
@app.route('/second')
def second():
  return "I'm on a separate route"


# HTTP Methods
@app.route('/request_generator', methods=['POST'])
def request_generator():
  if request.method == 'POST':
    quantity = int(request.form['quantity'])
    numbers = generate(quantity)
  return render_template('result.html', len = len(numbers), numbers = numbers)


# Redirects
@app.route('/redirect')
def redirec():
  return redirect(url_for('index'))



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
