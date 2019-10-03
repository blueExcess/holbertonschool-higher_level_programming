$.get('https://swapi.co/api/films/?format=json', (data) => {
  const results = data.results;
  for (const movie of results) {
    $('UL#list_movies').append($('<li></li>').text(movie.title));
  }
});
