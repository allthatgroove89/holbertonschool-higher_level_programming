// Select the element with id "add_item" and the ul element with class "my_list"
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

// Add a click event listener to the element with id "add_item"
addItem.addEventListener('click', () => {
    // Create a new li element
    const newListItem = document.createElement('li');

    // Set the text content of the new li element
    newListItem.textContent = 'Item';

    // Append the new li element to the ul element with class "my_list"
    myList.appendChild(newListItem);
});
