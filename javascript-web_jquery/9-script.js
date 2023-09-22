$(document).ready(function () {
  // Make an AJAX GET request to fetch translation data
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract the translation of "hello" from the response
    const helloTranslation = data.hello;

    // Display the translation in the DIV#hello element
    $('#hello').text(helloTranslation);
  });
});
