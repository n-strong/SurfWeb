import requests

# URL of the microservice endpoint (adjust the port if necessary)
url = 'http://127.0.0.1:333/send_forecast'

# Data to be sent (simulate form data)
data = {
    'email': 'fullstacktestingwebdev@gmail.com',  # Example email address
    'surf_forecast': 'Sunny with waves 3-5 feet'  # Example surf forecast data
}

# Make the POST request
response = requests.post(url, data=data)

# Print the response from the microservice
print('Response Status Code:', response.status_code)
print('Response Text:', response.text)
