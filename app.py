from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import sqlite3
import os
import json

app = Flask(__name__)

API_KEY = "695612f24ea951bbbc7c5dd8e52a5fcd"
DB_NAME = "weather.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    location TEXT,
                    date_range TEXT,
                    weather_data TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    date_range = request.form['date_range']

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return "Failed to retrieve weather data. Please try another location."

    weather_data = response.json()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO weather (location, date_range, weather_data) VALUES (?, ?, ?)",
              (location, date_range, json.dumps(weather_data)))
    conn.commit()
    conn.close()

    return redirect(url_for('history'))

@app.route('/history')
def history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    raw_records = c.fetchall()
    conn.close()

    # Parse weather JSON in Python
    records = []
    for r in raw_records:
        weather_data = json.loads(r[3])
        summary = {
            'id': r[0],
            'location': r[1],
            'date_range': r[2],
            'condition': weather_data['weather'][0]['main'],
            'temp': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity']
        }
        records.append(summary)

    return render_template('history.html', records=records)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM weather WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('history'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if request.method == 'POST':
        location = request.form['location']
        date_range = request.form['date_range']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            return "Failed to retrieve weather data."
        weather_data = response.json()
        c.execute("UPDATE weather SET location=?, date_range=?, weather_data=? WHERE id=?",
                  (location, date_range, json.dumps(weather_data), id))
        conn.commit()
        conn.close()
        return redirect(url_for('history'))
    else:
        c.execute("SELECT * FROM weather WHERE id=?", (id,))
        record = c.fetchone()
        conn.close()
        return render_template('update.html', record=record)

@app.route('/export')
def export():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    records = c.fetchall()
    conn.close()
    return jsonify(records)

@app.route('/info')
def info():
    return "<h3>PM Accelerator: Learn more about our company on <a href='https://www.linkedin.com/company/product-manager-accelerator/' target='_blank'>LinkedIn</a></h3>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

