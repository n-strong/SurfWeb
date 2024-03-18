from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import pysurfline
from io import BytesIO


app = Flask(__name__)

@app.route('/get_beach_data', methods=['POST'])
def get_beach_data():
    
    beach = request.json.get('beach_to_search')
      
    print(beach)
    port_forecasts = pysurfline.get_spot_forecasts(
        spotId=beach
    )
   
    output = BytesIO()
    pysurfline.plot_surf_report(port_forecasts, barLabels=True, wind=True)
    plt.savefig(output, format='png')
    output.seek(0)

    return send_file(output, mimetype='images/png')



if __name__ == "__main__":
    app.run(port=332, debug=True)