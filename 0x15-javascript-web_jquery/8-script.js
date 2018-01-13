$(document).ready((event) => {
  $.ajax({
    url: 'https://swapi.co/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    encode: 'true'
  })
    .done((data) => {
      const movies = data.results;
      movies.forEach(movie => {
        const title = movie.title;
        $('#list_movies').append(`<li>${title}</li>`);
      });
    });
});
