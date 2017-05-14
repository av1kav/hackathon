from flask import Flask, render_template
from flask import Response

import os
app = Flask(__name__)

print("Starting app...")

@app.route('/')
def index():
	return render_template('index.html')
	#hello!

@app.route('/location.html')
def location():
	return render_template('location.html')

@app.route('/suspect.html')
def suspect():
	return render_template('suspect.html')
#sddsads
if __name__ == "__main__":
	app.run(use_reloader=True,threaded=True)
