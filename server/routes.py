from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080, debug=True)