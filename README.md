# Flask Weather App

This is a full-stack weather tracking web application built with Python, Flask, and the OpenWeatherMap API. It was created as part of the PM Accelerator AI/ML Internship Technical Assessment.

The app allows users to:

- Search for real-time weather data by location (city or ZIP code)
- View temperatures in both Celsius and Fahrenheit
- Store searches in a SQLite database
- Update or delete stored records
- Export weather history as JSON
- View all search history
- See additional app and author information through a footer button


## Features

- Search for weather by city or ZIP code using the OpenWeatherMap API
- Save location and custom date range input to a local database
- View full history of saved searches
- Edit or delete existing weather records
- Export entire weather history as a JSON file
- Informational route linking to the PM Accelerator company page
- All features implemented using Flask, Jinja2, and clean HTML templates


## Technologies Used

- Python 3
- Flask
- SQLite
- HTML/CSS
- OpenWeatherMap API
- Jinja2 Templates

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

API_KEY = "695612f24ea951bbbc7c5dd8e52a5fcd"


---

## Info Route

The app includes an informational `/info` route that displays a brief description of the PM Accelerator program. You can learn more about the organization via their [LinkedIn page](https://www.linkedin.com/school/pmaccelerator/).

---

## Author

Eakraj Raut  
GitHub: [eakraj10](https://github.com/eakraj10)
