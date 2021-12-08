const apiUrl = "https://vro6z6n156.execute-api.us-east-1.amazonaws.com/test";



fetch(apiUrl)
.then(response => response.json())
.then(result => document.getElementById('visitor_counter').innerHTML = result + ' people checked out this resume.')
.catch(error => console.log('error', error));



