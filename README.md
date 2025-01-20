# Side-by-Sky 🌤️
### Version 0.1.0

A weather comparison app built with Flask that allows you to compare weather conditions between your location and a friend's. The app fetches data from the OpenWeather API and displays the weather details in an easy-to-read format.

## Features
- 🌍 **Compare weather** between two locations.
- 📈 Shows **temperature, humidity, and weather conditions**.
- 🎨 Beautiful, responsive UI with Bootstrap.
- 🔒 Secure API key management using `.env`.

---
<img width="1688" alt="Screenshot 2025-01-19 at 04 10 18" src="https://github.com/user-attachments/assets/c3125aaf-7096-4413-abc7-ec157c37c15a" />

## Getting Started

### Prerequisites
1. **Python**: Install [Python 3.8+](https://www.python.org/downloads/).
2. **pip**: Ensure `pip` is installed for package management.
3. **API Key**: Sign up for an [OpenWeather API Key](https://home.openweathermap.org/api_keys).

### Installation
1. **Clone the repository**: // Or simply download files from this repository
   ```bash
   git clone https://github.com/Leoxoo/Side-by-Sky.git
   cd Side-by-Sky
   ```
    Or simply download files from the repository

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenWeather API key:
   ```
   API_KEY=your_openweather_api_key
   ```

---

### Usage
1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the app**:
   Open your browser and navigate to: IP that is provided in your terminal

3. **Using the app**:
   - Enter your city, state, and country to get weather data.
   - Enter your friend's location for a side-by-side comparison.
   - See temperature, humidity, and weather conditions for both locations.

---


## Project Structure
```
├── app.py               # Main Flask app
├── weather.py           # Weather fetching logic
├── templates/           # HTML templates for the app
│   ├── index.html       # Main page
│   └── settings.html    # Settings page
├── static/              # Static files (CSS, images)
├── .env                 # API key (excluded from Git)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Author
Created by **Leonid Mateush**.

Feel free to connect or report issues in the [issues section](https://github.com/yourusername/side-by-sky/issues).
