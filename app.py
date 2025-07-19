import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv # Import load_dotenv
load_dotenv() # Load environment variables from .env file
PNR_RAPIDAPI_KEY = "70a5122ed8msh805ba414bc5366dp10535ejsndb7025a72dde"
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_pnr', methods=['GET', 'POST']) # <--  Add 'GET' here
def check_pnr():
    if request.method == 'POST':  # Handle POST requests when the form is submitted
        pnr_number = request.form['pnr_number']

        url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr_number}"
        headers = {
            'x-rapidapi-host': "irctc-indian-railway-pnr-status.p.rapidapi.com",
            'x-rapidapi-key': PNR_RAPIDAPI_KEY
        }

        try:
            response = requests.request("GET", url, headers=headers)
            response.raise_for_status()

            print(f"Raw API Response Status Code: {response.status_code}")
            print(f"Raw API Response Content (text): {response.text}")

            pnr_status = response.json()

            print(f"Parsed JSON Response: {pnr_status}")

            if response.status_code == 200:
                return render_template('pnr_result.html', pnr_status=pnr_status)
            elif response.status_code == 404:
                return render_template('pnr_result.html', pnr_status={"error": "PNR number not found. Please check and try again."})
            else:
                return render_template('pnr_result.html', pnr_status={"error": f"API Error: {pnr_status.get('message', 'Unknown error')}"})

        except requests.exceptions.RequestException as e:
            print(f"Network Error during API call: {e}")
            return render_template('pnr_result.html', pnr_status={"error": f"Network Error: {e}"})
        except ValueError:
            print(f"ValueError: Failed to parse API response as JSON. Raw response: {response.text}")
            return render_template('pnr_result.html', pnr_status={"error": "Failed to parse API response. Please try again later."})
    else:  # Handle GET requests (e.g., if someone directly navigates to /check_pnr)
        return render_template('index.html') # Or redirect, or show an error

if __name__ == '__main__':
    app.run(debug=True)
