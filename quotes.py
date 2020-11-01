from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:very_strong_password@localhost/quotes'
# config for heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mtaidfxoafxhuz:b25df59b9d95190d7758df7cde70580bf8a116fb66efeb3436a5ba793e91cfda@ec2-54-228-250-82.eu-west-1.compute.amazonaws.com:5432/d502ibglh4uh1v'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))
#     Then, launch the python shell in root project directory,
#     enter the following to create tables in the database:
#           from flask_sqlalchemy import SQLAlchemy
#           db.create_all()


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
