function sendData() {
    let beach = document.getElementById("search").value;

    fetch('/search_beaches', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(beach)
    })
    .then(response =>{
        if(!response.ok) {
            throw new Error ('Error in network response.');
        }
        window.location.href = response.url;
        return response.json();
    })
    .then(data => {
        console.log('Response from server:', data);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error)
    })
}

function goHome() {
    window.location.href = '/'
}

function getForecast(){
    fetch('/forecast')
    .then(response => {
        if (!response.ok){
            throw new Error('Network response was not ok');
        }
        window.location.href = response.url;
        return response.text();
    })
    .then(data => {
        console.log('Forecast: ', data);
    })
    .catch(error =>{
        console.error('There was a problem with the fetch operation:', error);
    });
}