const redHeader = document.querySelector('#red_header');
const header = document.querySelector('h1');

redHeader.addEventListener('click', () => {
  header.classList.add('red');
});
