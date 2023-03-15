import random
counter = 0
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("numeri4.html") 

@app.route('/risultato/<numero>')
def risultato(numero):
  global counter
  counter += 1  
  casuale = random.randint(1,9)
  if casuale == int(numero):
    return render_template("risultato3.html", hai = f'Hai vinto!!! Hai scelto {numero} e il numero era {casuale}', volte = counter)
  else:
    return render_template("risultato3.html", hai = f'Hai perso!!! Hai scelto {numero} ma il numero era {casuale}', volte = counter)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3275, debug=True)