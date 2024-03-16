from flask import Flask, request, jsonify
import pysurfline


app = Flask(__name__)

@app.route('/get_beach_data', methods=['POST'])
def get_beach_data():
    
    beach = request.json.get('beach_to_search')
      
    print(beach)
    port_forecasts = pysurfline.get_spot_forecasts(
        spotId=beach,
        days=2,
        intervalHours=3
    )
   
    port_forecasts = {str(port_forecasts.name): 
                        [
                        str(port_forecasts.sunlightTimes), str(port_forecasts.tides), 
                        str(port_forecasts.weather),
                        str(port_forecasts.wind)
                        ]}
    
    return jsonify(port_forecasts)



if __name__ == "__main__":
    app.run(port=332, debug=True)