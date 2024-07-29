// URL of the API endpoint
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Function to fetch the hello translation
function fetchHello() {
    fetch(url)
        .then(response => {
            // Check if the response is okay (status code 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Parse the response as JSON
        })
        .then(data => {
            // Update the text content of the element with the translation
            document.querySelector('#hello').textContent = data.hello;
        })
        .catch(error => {
            // Handle any errors that occur during the fetch
            console.error('Error fetching translation:', error);
            document.querySelector('#hello').textContent = 'Failed to fetch translation';
        });
}

// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', fetchHello);
