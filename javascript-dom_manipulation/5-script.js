// Select the element with id "update_header" and the header element
const updateHeaderButton = document.querySelector('#update_header');
const header = document.querySelector('h1');

// Add a click event listener to the element with id "update_header"
updateHeaderButton.addEventListener('click', () => {
    // Update the text content of the header element
    header.textContent = 'New Header!!!';
});
