from flask import Flask,render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['counter']=0
    session['random']=random.randint(1,100)
    print(session['random'])
    return render_template('index.html')

@app.route('/verify', methods=['post'])
def verify():
    if session['counter']==4:
            return render_template('lost.html')
    session['num']=int(request.form['number_guessed'])
    if session['num']>session['random']:
        session['counter']+=1
        return render_template('too_hight.html')
    elif session['num']<session['random']:
        session['counter']+=1
        return render_template('too_low.html')
    else:
        session['counter']+=1
        return render_template('win.html')

@app.route('/winner', methods=['post'])
def add_winner():
    session['name']=request.form['name']
    return render_template('winner.html')


if __name__ == '__main__':
    app.run(debug=True)