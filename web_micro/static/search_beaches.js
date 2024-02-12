function sendData() {
    let beach = document.getElementById("search").value;

    fetch('/search_beaches', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'beaches to search': beach})
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