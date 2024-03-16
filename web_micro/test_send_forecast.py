import requests

# URL of the microservice endpoint (adjust the port if necessary)
url = 'http://127.0.0.1:333/send_forecast'

data1 = requests.post('http://localhost:332/get_beach_data', json={'beach_to_search': '5842041f4e65fad6a7708976'})

print('Status code from surf_data.py: ', data1.status_code)

# Data to be sent (simulate form data)
data = {
    'email': 'fullstacktestingwebdev@gmail.com',  # Example email address
    'surf_forecast': '${data1.json}' # Example surf forecast data
}

# Make the POST request
response = requests.post(url, data=data)

# Print the response from the microservice
print('Response Status Code:', response.status_code)
print('Response Text:', response.text)
