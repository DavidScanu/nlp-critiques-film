import requests
from flask import Flask, render_template, request, redirect, url_for, flash


# CONSTANTS
VERBOSE = True

# Flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


if __name__=='__main__':
   app.run()


@app.route("/", methods=['GET', 'POST'])
def index():

	if request.method == "POST":
		comment_user = request.form.get("comment-user")
		return redirect(url_for('index'))
	else:
		return render_template('index.html')