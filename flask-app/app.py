import pickle
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from modules.clean_text import clean_text

# CONSTANTS
VERBOSE = True

# Import pickle data 
pickle_in = open("model.pkl","rb")
dict_import = pickle.load(pickle_in)
pickle_in.close()

# Variables
model_best = dict_import['model_best']
tfidf = dict_import['tfidf']

def predict_comment(comment):

	comment_clean = clean_text(comment)
	comment_tfidf = tfidf.transform([comment_clean])
	pred = model_best.predict(comment_tfidf)
	# convert ndarray float to python int
	pred_int = pred[0].astype(int).item()
	return pred_int

# Flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__=='__main__':
   app.run()

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		comment_user = request.form.get("comment-user")
		prediction = predict_comment(comment_user)
		# return redirect(url_for('index', prediction=prediction))
		return render_template('index.html', prediction=prediction, comment_user=comment_user)
	else:
		return render_template('index.html')
