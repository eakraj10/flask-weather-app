# Flask Weather App

This project is a full-stack weather tracking web application built using Python and Flask. It was created for the PM Accelerator AI/ML Internship Technical Assessment.

The app allows users to search for real-time weather data using the OpenWeatherMap API and store the results in a local SQLite database. Users can manage their entries through a full CRUD (Create, Read, Update, Delete) interface, and also export stored data as JSON.

---

## Features

- Search weather by city or location using OpenWeatherMap API
- Save location and custom date range input to local database
- View full history of saved searches
- Edit or delete existing weather records
- Export entire weather history as a JSON endpoint
- Informational route with PM Accelerator company link
- All features implemented using clean Flask and Jinja2 templates

---

## Technologies Used

- Python 3
- Flask
- HTML (Jinja2 Templates)
- SQLite (via `sqlite3`)
- OpenWeatherMap API
- CSS (basic styling)

---

## Getting Started

### Clone the repository:

```bash
git clone https://github.com/eakraj10/flask-weather-app.git
cd flask-weather-app
```

### Create virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask app


python app.py
```

API_KEY = "your_actual_api_key_here"

---

## Info Route

The app includes an informational `/info` route that displays a brief description of the PM Accelerator program. You can learn more about the organization via their [LinkedIn page](https://www.linkedin.com/school/pmaccelerator/).

---

## Author

Eakraj Raut  
GitHub: [eakraj10](https://github.com/eakraj10)
