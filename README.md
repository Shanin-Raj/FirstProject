# My Python Learning Projects

This repository is a collection of my first projects as I learn Python, APIs, and best practices for coding.

## Projects Included

* **`greetings.py`**: A script that uses the Google Gemini API to generate a unique greeting based on a historical event from the current date.
* **`weather.py`**: A script that uses the OpenWeatherMap API to fetch and display the current weather for a specific city.

## How to Run These Projects

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shanin-Raj/FirstProject.git](https://github.com/Shanin-Raj/FirstProject.git)
    cd FirstProject
    ```

2.  **Create your `.env` file:**
    Create a file named `.env` and add your API keys. You will need one for each project.
    ```
    GEMINI_API_KEY=YOUR_GEMINI_KEY_HERE
    OPENWEATHER_API_KEY=YOUR_OPENWEATHER_KEY_HERE
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run a script!**
    ```bash
    python greetings.py
    ```
    or
    ```bash
    python weather.py
    ```
