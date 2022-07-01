from urllib import request
from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__, 
            static_folder='./static',
            template_folder='./templates')
app.secret_key = "dadasdasdas"
@app.route('/')
def main():
    return render_template("strona_glowna.html")
@app.route('/tworcy')
def creators():
    return render_template("tworcy.html")
@app.route('/plot', methods=["POST","GET"])
def plot():
    #f=request.form['natężenie_pola']
    #g=request.form['indukcja_pola_1']
    #h=request.form['indukcja_pola_2']
    #l=request.form['prędkość_cząstki']
    r=3
    q=5
    stepsize=0.1
    
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
    
    plt.plot(y, x)
    plt.savefig('/static/images/plot.png')

    return render_template('index.html', url='/static/images/plot.png')

if __name__ == '__main__':
   app.run()
