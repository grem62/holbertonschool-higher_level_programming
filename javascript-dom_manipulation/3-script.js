// selectionne le toggle_header
const selectorClick = document.querySelector('#toggle_header');

const selectorHeader = document.querySelector('header');

selectorClick.addEventListener('click', function () {
  // Toggle the class of the header element between "red" and "green"
  selectorHeader.classList.toggle('red');
  selectorHeader.classList.toggle('green');
});
