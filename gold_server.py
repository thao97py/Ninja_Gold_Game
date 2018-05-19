from flask import Flask, render_template, request, redirect, session
from flask import Markup
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key='hj48n9n798n9n87dgh%&'

@app.route('/')
def index():
    if 'earn' not in session:
        session['earn']=0
    if 'activity' not in session:
        session['activity']=[] 
    
    return render_template('/gold.html', gold=session['earn'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def process():
    date= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if 'earn' not in session:
        session['earn']=0
    if 'activity' not in session:
        session['activity']=[]

    if request.form['building']=='farm':
        gold=random.randrange(10,21)
        session['earn'] += gold
        session['activity'].append({"Event":"Earned %s golds from the farm! (%s) " %( gold, date),
                                    "won":True})
     
    elif request.form['building']=='cave':
        gold=random.randrange(5,11)
        session['earn'] += gold
        session['activity'].append({"Event":"Earned %s golds from the cave! (%s) " %( gold, date),
                                    "won":True})
    elif request.form['building']=='house':
        gold=random.randrange(2,6)
        session['earn'] += gold
        session['activity'].append({"Event":"Earned %s golds from the house! (%s) " %( gold, date),
                                    "won":True})
    else:
        gold=random.randrange(0,51)
        give_or_take = random.randrange(0,2)
        if give_or_take ==0:
            session['earn'] -=gold
            session['activity'].append({"Event":"Entered a casino and lost %s golds... Ouch...(%s) " %( gold, date),
                                        "won":False})
        elif give_or_take==1:
            session['earn'] +=gold
            session['activity'].append({"Event":"Entered a casino and earned %s golds... Yay!...(%s) " %( gold, date),
                                        "won":True})
        print "get", give_or_take, "at Casino" 
   
    return redirect('/')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)