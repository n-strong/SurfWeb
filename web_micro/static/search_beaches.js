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
        return response.json();
    })
    .then(beach => {
        console.log('Response from server:', beach);
    })
    .catch(error => {
        console.error('Error with fetch operation:', error)
    })
}