from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Function to determine zodiac sign based on birthday
def get_zodiac_sign(birthday):
    month, day = int(birthday.split("-")[1]), int(birthday.split("-")[2])
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "pisces"

# Function to get horoscope from API
def get_horoscope(zodiac_sign):
    url = f"https://aztro.sameerkumar.website/?sign={zodiac_sign}&day=today"
    response = requests.post(url)  # This API requires a POST request
    if response.status_code == 200:
        data = response.json()
        return data['description']
    else:
        return "Sorry, we couldn't retrieve your horoscope at this moment."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horoscope', methods=['POST'])
def horoscope():
    name = request.form['name']
    birthday = request.form['birthday']
    
    # Determine zodiac sign
    zodiac_sign = get_zodiac_sign(birthday)

    # Fetch horoscope from API
    horoscope = get_horoscope(zodiac_sign)
    
    return render_template('horoscope.html', name=name, birthday=birthday, zodiac_sign=zodiac_sign, horoscope=horoscope)

if __name__ == '__main__':
    app.run(debug=True)
