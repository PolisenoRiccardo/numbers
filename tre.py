import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("numeri3.html") 

@app.route('/risultato/<numero>')
def risultato(numero):
  casuale = random.randint(1,9)
  if casuale == int(numero):
    return render_template("risultato.html", hai = f'Hai vinto!!! Hai scelto {numero} e il numero era {casuale}')
  else:
    return render_template("risultato.html", hai = f'Hai perso!!! Hai scelto {numero} ma il numero era {casuale}')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)