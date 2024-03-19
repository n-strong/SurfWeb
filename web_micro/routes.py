from flask import Flask, render_template, request, redirect, jsonify
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import base64


app = Flask(__name__)
SURF_DATA_URL = 'http://localhost:332/get_beach_data'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search_beaches', methods=['GET', 'POST'])
def search_beaches():
    if request.method == 'POST':
        
        beach = request.form.get('beach')
            
        global spotID    
        spotID = get_spotID(beach)

        beach_names = [i for i in spotID.keys()]
        
        return render_template('search_results.html', beach=beach_names)

    else:
        redirect('/')

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
    # surf_forecast = request.form['surf_forecast']
    
    surf_forecast_image = surf_forecast
    msg = MIMEMultipart()
    
    msg['From'] = 'fullstacktestingwebdev@gmail.com'
    msg['To'] = email_address
    msg['Subject'] = 'Your Surf Forecast'
    
    body = 'Here is your surf forecast: '
    
    msg.attach(MIMEText(body, 'plain'))
    image_part = MIMEImage(surf_forecast_image)
    image_part.add_header('Content-Disposition', 'attachment', filename='surf_forecast.png')
    msg.attach(image_part)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('fullstacktestingwebdev@gmail.com', 'jkaa zdwk fntj wcdh')
    text = msg.as_string()
    server.sendmail('fullstacktestingwebdev@gmail.com', email_address, text)
    server.quit()
    return jsonify({'message': 'Email sent successfully!'})


@app.route('/forecast', methods=['POST'])
def show_forecast():
    beach = request.form.get('beach name')
    print(beach)

    if beach in spotID.keys():
        response = requests.post(SURF_DATA_URL, json={'beach_to_search': spotID.get(beach)})
        
        global surf_forecast
        surf_forecast = response.content 
        
        surf_forecast_image = base64.b64encode(surf_forecast).decode('utf-8')
    
        return render_template('forecast.html', surf_forecast=surf_forecast_image)
    
    else:
        return 'Error fetching surf forecast', 500

if __name__ == '__main__':
    app.run(port=333)
