from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)
SURF_DATA_URL = 'http://localhost:332/get_beach_data'

@app.route('/')
def home():
    return render_template("index.html") 


@app.route('/search_beaches', methods=['POST'])
def search_beaches():
    
    # beach = request.json()
    beach = '5cbf8d85e7b15800014909e8' 
    # print('Response received: ', beach)
    response = requests.post(SURF_DATA_URL, json={'beach_to_search': beach}, verify=False)
    test = response.json() 
    print(jsonify(test))
     
    return redirect('search_results')

@app.route('/search_results')
def search_results():
    return render_template('search_results.html') 


if __name__ == '__main__':
    app.run(port=333)  
   
   
   
   
