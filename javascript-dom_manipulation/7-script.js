// URL of the API endpoint
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Select the ul element with id "list_movies"
const listMovies = document.querySelector('#list_movies');

// Fetch the movie data from the API
fetch(url)
    .then(response => {
        // Check if the response is okay (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        // Iterate through the films array and create list items for each movie title
        data.results.forEach(film => {
            // Create a new li element
            const listItem = document.createElement('li');

            // Set the text content of the li element to the film title
            listItem.textContent = film.title;

            // Append the li element to the ul element
            listMovies.appendChild(listItem);
        });
    })
    .catch(error => {
        // Handle any errors that occur during the fetch
        console.error('Error fetching movie data:', error);
        listMovies.textContent = 'Failed to fetch movie titles';
    });