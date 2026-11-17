# 🌤️ Real-Time Weather Application

## Project Overview
A real-time weather application developed using Python, WeatherAPI, and Streamlit. Users can search for weather information by entering a city name and select which weather details they want to display.

## Features
- Search weather information by city name.
- Display real-time weather conditions.
- Select Celsius or Fahrenheit.
- Display temperature and feels-like temperature.
- Choose weather details such as:
  - Humidity
  - Wind speed
  - Wind direction
  - Atmospheric pressure
  - Visibility
  - Last updated time
- Handle invalid city names and API errors.

## Technologies Used
- Python
- Requests
- Streamlit
- WeatherAPI
- Python-dotenv

## Project Structure

```text
WeatherAPI_Project/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the project directory:

```text
WEATHER_API_KEY=YOUR_API_KEY
```

Never upload your `.env` file to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

## API Provider
Weather data is provided by WeatherAPI.

https://www.weatherapi.com/

## Author
Srihari Ravanam