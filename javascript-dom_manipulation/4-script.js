// Find the button element with the id "add_item"
const clickAddItem = document.querySelector('#add_item');

// Find the ul element with the class "my_list"
const myList = document.querySelector('.my_list');

// Add a click event listener to the button
clickAddItem.addEventListener('click', function () {
  // Create a new list item element
  const newItem = document.createElement('li');

  // Set the text content of the new item
  newItem.textContent = 'Item';

  // Append the new item to the ul element
  myList.appendChild(newItem);
});
