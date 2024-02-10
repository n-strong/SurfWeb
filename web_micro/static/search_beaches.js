let beach = document.getElementByID('search_button');

search_button.addEventListener('click', sendData)

console.log('here 1')

function sendData(){
    let beach = document.getElementByID("text_input").value;

    fetch("/search_beaches", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'beaches to search': beach})
    })
    .then(response => {
        if(!response.ok) {
            throw new Error('Error in network response');
        }
        console.log('here!')
        return response.json();
    })
    .then(beach => {
        console.log('Response from server:', beach);
    })
    .catch(error =>{
        console.error('Error with fetch operation:', error)
    });
}