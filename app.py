from urllib import request
from flask import Flask, render_template, request, flash
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__, 
            static_folder='./static',
            template_folder='./templates')
app.secret_key = "dadasdasdas"
@app.route('/')
def main():
    return render_template("strona_glowna.html", methods=["POST","GET"])
@app.route('/tworcy')
def creators():
    return render_template("tworcy.html", methods=["POST","GET"])

@app.route('/plot', methods=["POST", "GET"])
def licz():
    return render_template('index.html')

@app.route('/wynik', methods=["POST","GET"])
def calculate():
    e=float(request.form['natężenie_pola'])
    b1=float(request.form['indukcja_pola_1'])
    b2=float(request.form['indukcja_pola_2'])
    v=float(request.form['prędkość_cząstki'])
    q=float(request.form['ładunek'])
    r=float(request.form['promień'])
    if abs(e - v*b1)< 0.0000000001 :
        masa_cala=abs(q)*b2*r*6.022136651675e+16/v
        m=round(masa_cala, 4)
    else:
        m='nie zmierzona, ponieważ nie ma cząstka nie porusza się ruchem jednostajnym'
    flash("masa "+ str(m)+" u")\
    
    stepsize=0.001*r
    if abs(e - v*b1)< 0.0000000001 :
        if q > 0:
            x = np.arange(0, r+stepsize, stepsize)
            y = np.sqrt(r**2 - x**2)

            x = np.concatenate([x,x[::-1]])

            y = np.concatenate([y,-y[::-1]])

            x, y = x, y + r
        else:
            x = np.arange(0, r+stepsize, stepsize)
            y = np.sqrt(r**2 - x**2)

            x = np.concatenate([x,x[::-1]])

            y = np.concatenate([y,-y[::-1]])

            x, y = x , -y - r
    else:
        x,y = 0, 0
    
    
    plt.plot([-r*0.01, -r*0.005, r*0.005, r*0.01], [0, r*0.005, r*0.005, 0], color='r')
    plt.plot([-r*2, r*2], [0, 0], color='k')
    plt.plot(y, x, color='b')
    plt.grid(True,  which='both')
    plt.xlabel("x cm")
    plt.ylabel("y cm")
    plt.title("Wykres ruchu czastki w polu magnetycznym ")
    plt.savefig('./static/plot.png')
    plt.close("all")

    return render_template('index.html', url="plot.png")
 
if __name__ == '__main__':
   app.run(port=5001)
