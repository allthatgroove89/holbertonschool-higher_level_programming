// URL of the API endpoint
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Select the element with id "character"
const characterElement = document.querySelector('#character');

// Fetch the character data from the API
fetch(url)
    .then(response => {
        // Check if the response is okay (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        // Update the text content of the element with the character name
        characterElement.textContent = data.name;
    })
    .catch(error => {
        // Handle any errors that occur during the fetch
        console.error('Error fetching character data:', error);
        characterElement.textContent = 'Failed to fetch character name';
    });
