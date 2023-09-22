$(document).ready(function () {
  // Make an AJAX GET request to fetch movie data
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    // Loop through the movie data and append titles to the UL#list_movies
    $.each(data.results, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
