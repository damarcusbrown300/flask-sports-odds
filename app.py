from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.now().strftime('%Y-%m-%d')
    url = f"https://www.balldontlie.io/api/v1/games?start_date={today}&end_date={today}"
    response = requests.get(url)
    
    if response.status_code == 200:
        games = response.json().get('data', [])
    else:
        games = []

    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
