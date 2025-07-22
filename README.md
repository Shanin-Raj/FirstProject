# Historical Greeting Generator

This is a simple Python script that generates a unique, one-sentence greeting based on a historical event that happened on the current day. It uses the Google Gemini API to generate the creative greeting.

This was my first project using an API and setting up a secure repository for GitHub.

## Features

-   Gets the current date automatically.
-   Calls the Gemini API with a dynamic prompt.
-   Securely loads an API key from a `.env` file.

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shanin-Raj/FirstProject.git](https://github.com/Shanin-Raj/FirstProject.git)
    ```

2.  **Navigate into the directory:**
    ```bash
    cd FirstProject
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file for this command to work).*

4.  **Create your `.env` file:**
    Create a file named `.env` in the main project folder and add your API key to it:
    ```
    GEMINI_API_KEY=YOUR_OWN_API_KEY_HERE
    ```

5.  **Run the script!**
    ```bash
    python greetings.py
    ```

