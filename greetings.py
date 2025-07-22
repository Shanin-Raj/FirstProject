# -*- coding: utf-8 -*-
"""
A simple Python script to generate a unique greeting based on a historical
event from the current date using the Gemini API.

FINAL FIX: This version cleans the text to remove special characters
that can cause crashes on some Windows terminals.
"""

# Import necessary libraries
import requests
import datetime
import os

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
        # --- Step 1: Get your API Key ---
        # Get your key from Google AI Studio: https://aistudio.google.com/app/apikey
        api_key = "AIzaSyBjmSH1K_M60dOAe0iBAHpAqnU6KfR5g2c" # <-- IMPORTANT: Paste your API key here!

        if "YOUR_API_KEY_HERE" in api_key:
            print("Error: Please replace 'YOUR_API_KEY_HERE' with your actual Gemini API key.")
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
            
            # --- THIS IS THE NEW FIX ---
            # We clean the text by encoding it to ASCII and ignoring any characters
            # (like emojis) that it can't represent. Then we decode it back.
            cleaned_text = generated_text.strip().encode('ascii', 'ignore').decode('ascii')
            
            print("\n--- Your Historical Greeting ---")
            print(cleaned_text) # Print the cleaned text
            print("------------------------------\n")
        else:
            print("Error: Could not find a valid response from the API.")
            print("Full response:", data)

    except requests.exceptions.RequestException as e:
        # This block now includes a more specific message for encoding errors
        if isinstance(e, UnicodeEncodeError):
             print(f"An encoding error occurred: {e}. The script tried to fix this but failed.")
        else:
            print(f"An error occurred with the API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This is the standard Python entry point.
if __name__ == "__main__":
    generate_greeting()

