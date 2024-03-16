from flask import Flask, render_template, request, redirect, jsonify
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
SURF_DATA_URL = 'http://localhost:332/get_beach_data'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search_beaches', methods=['GET', 'POST'])
def search_beaches():
    if request.method == 'POST':
        
        beach = request.form.get('beach')
            
        spotID = get_spotID(beach)
        
        return render_template('search_results.html', beach_name=beach)

    else:
        redirect('/')

    # return redirect('search_results')

def get_spotID(location: str):
    url = 'https://services.surfline.com/search/site' 
    params = {'q': location}
    response = requests.get(url, params=params)
    
    spotID_dict = {}
    
    if response.status_code == 200:
    
        for item in response.json():
            if 'hits' in item and 'hits' in item['hits']:
                for hit in item['hits']['hits']:
                    spotID_dict.update({hit.get('_source').get('name'): hit.get('_id')})
        
        print(spotID_dict)
        return spotID_dict
    
    else:
        return {'error': 'Request failed', 'status_code': response.status_code}
     


@app.route('/send_forecast', methods=['POST'])
def send_forecast():
    email_address = request.form['email']
    surf_forecast = request.form['surf_forecast']
    msg = MIMEMultipart()
    msg['From'] = 'fullstacktestingwebdev@gmail.com'
    msg['To'] = email_address
    msg['Subject'] = 'Your Surf Forecast'
    body = 'Here is your surf forecast: ' + surf_forecast
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('fullstacktestingwebdev@gmail.com', 'jkaa zdwk fntj wcdh')
    text = msg.as_string()
    server.sendmail('fullstacktestingwebdev@gmail.com', email_address, text)
    server.quit()
    return jsonify({'message': 'Email sent successfully!'})

@app.route('/forecast')
def show_forecast():
    response = requests.post(SURF_DATA_URL, json={'beach_to_search': spotID}) 
    surf_forecast = jsonify(response.text)
    return render_template('forecast.html', surf_forecast=surf_forecast.json)

if __name__ == '__main__':
    app.run(port=333)
