# -*- coding: utf-8 -*-
"""
A simple Python script to generate a unique greeting based on a historical
event from the current date using the Gemini API.

"""

# Import necessary libraries
import os
import requests
import datetime
from dotenv import load_dotenv 


load_dotenv()

def get_date_with_suffix(d):
    """
    Adds the correct ordinal suffix (st, nd, rd, th) to a day of the month.
    """
    return str(d) + ("th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th"))

def generate_greeting():
    """
    Main function to get the date, call the Gemini API, and print the response.
    """
    try:
        # --- Step 1: Load the API key from the .env file ---
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("Error: GEMINI_API_KEY not found in .env file.")
            print("Please create a .env file and add your key to it.")
            return

        # --- Step 2: Get the current date and format it ---
        today = datetime.date.today()
        day_with_suffix = get_date_with_suffix(today.day)
        formatted_date = today.strftime(f"%B {day_with_suffix}")

        print(f"Requesting a greeting for today: {formatted_date}")

        # --- Step 3: Construct the prompt for the API ---
        prompt = f"Give me a unique one-sentence greeting based on something interesting that happened on {formatted_date} in history."

        # --- Step 4: Prepare and send the request to the Gemini API ---
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()

        # --- Step 5: Parse the response and print the result ---
        data = response.json()

        if 'candidates' in data and data['candidates']:
            generated_text = data['candidates'][0]['content']['parts'][0]['text']
            cleaned_text = generated_text.strip().encode('ascii', 'ignore').decode('ascii')
            
            print("\n--- Your Historical Greeting ---")
            print(cleaned_text)
            print("------------------------------\n")
        else:
            print("Error: Could not find a valid response from the API.")
            print("Full response:", data)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This is the standard Python entry point.
if __name__ == "__main__":
    generate_greeting()


