from app import app

@app.route('/')
def home():
	return "<h1> Hello Chetan and Aditya </h1>"