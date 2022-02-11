$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    results = data.results;
    for (let i = 0; i < results.length; i++) { $('ul#list_movies').append(`<li>${results[i].title}</li>`); }
  });
