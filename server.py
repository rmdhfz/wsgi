
from flask import Flask

app = Flask(__name__)
@app.route('/')

def welcome():
	return 'Hi'

@app.route('/home/introduction')

def introduction():
	return 'The introduction() is called'

if __name__ == '__main__':
	app.run()