const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('h1');
// Add a click event listener to the element with id "toggle_header"
toggleHeader.addEventListener('click', () => {
  // Check the current class and toggle between 'red' and 'green'
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
} else {
    header.classList.replace('green', 'red');
}
});
