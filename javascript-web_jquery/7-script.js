// Use jQuery to make an AJAX GET request to the API URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  // Extract the character name from the response data
  const characterName = data.name;
});
