from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3
import json

app = Flask(__name__)

API_KEY = "695612f24ea951bbbc7c5dd8e52a5fcd"

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 location TEXT,
                 date_range TEXT,
                 weather_data TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    date_range = request.form['date_range']

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conn = sqlite3.connect('weather.db')
        c = conn.cursor()
        c.execute("INSERT INTO weather (location, date_range, weather_data) VALUES (?, ?, ?)",
                  (location, date_range, json.dumps(data)))
        conn.commit()
        conn.close()
        return redirect(url_for('history'))
    else:
        return "Error retrieving weather data"

@app.route('/history')
def history():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    records = c.fetchall()
    conn.close()
    parsed_records = []
    for record in records:
        data = json.loads(record[3])
        temp_c = data['main']['temp']
        temp_f = round((temp_c * 9/5) + 32, 2)
        description = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        parsed_records.append((record[0], record[1], record[2], temp_c, temp_f, description, humidity))
    return render_template('history.html', records=parsed_records)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("DELETE FROM weather WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('history'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    if request.method == 'POST':
        location = request.form['location']
        date_range = request.form['date_range']
        c.execute("UPDATE weather SET location=?, date_range=? WHERE id=?", (location, date_range, id))
        conn.commit()
        conn.close()
        return redirect(url_for('history'))

    c.execute("SELECT * FROM weather WHERE id=?", (id,))
    record = c.fetchone()
    conn.close()
    return render_template('update.html', record=record)

@app.route('/export')
def export():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    records = c.fetchall()
    conn.close()
    data = [{"id": r[0], "location": r[1], "date_range": r[2], "weather": json.loads(r[3])} for r in records]
    return json.dumps(data, indent=4)

@app.route('/info')
def info():
    return redirect("https://www.linkedin.com/school/pmaccelerator/")

if __name__ == '__main__':
    app.run(debug=True)
