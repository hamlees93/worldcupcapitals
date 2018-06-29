from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from capital import capital, country, country_length
from werkzeug.wrappers import Request

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
  return render_template('home.html',
  	country=country,
  	country_length=country_length,
  	capital=capital)

@app.route('/results', methods=['POST'])
def results():
  count = 0
  guess = []
  correct_integer = []
  incorrect_integer = []
  for i in range(country_length):
  	guess.append(request.form[str(i)])
  	if guess[i].lower() == capital[i][0].lower() or guess[i] == capital[i][1].lower():
  	  count += 1
  	  correct_integer.append(i)
  	else:
  	  incorrect_integer.append(i)
  return render_template('results.html',
    country_length=country_length,
  	count=count,
  	country=country,
  	capital=capital,
  	guess=guess,
  	correct_integer=correct_integer,
  	incorrect_integer=incorrect_integer
  	)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5500,debug=True)