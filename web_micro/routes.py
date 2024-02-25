from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)
SURF_DATA_URL = 'http://localhost:332/get_beach_data'

@app.route('/')
def home():
    return render_template("index.html") 


@app.route('/search_beaches', methods=['POST'])
def search_beaches():
    spotID_dict = {'Pacifica, California': '5842041f4e65fad6a7708976'}
    
    beach = request.json
   
    if beach in spotID_dict.keys():
        spotID = spotID_dict[beach]
    
    global response 
   
    response = requests.post(SURF_DATA_URL, json={'beach_to_search': spotID})

    
    return redirect('search_results')

@app.route('/search_results')
def search_results():
    return render_template('search_results.html') 

@app.route('/forecast')
def show_forecast():
    surf_forecast = jsonify(response.text)

    return render_template('forecast.html', surf_forecast=surf_forecast.json)
if __name__ == '__main__':
    app.run(port=333)  
   
   
   
   
