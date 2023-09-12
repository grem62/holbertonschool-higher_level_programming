const interaction = document.querySelector('#red_header');

// Select the header element by its ID
const headerElement = document.querySelector('header');

// Add a click event listener to the button
interaction.addEventListener('click', function () {
  // Update the text color of the header to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
