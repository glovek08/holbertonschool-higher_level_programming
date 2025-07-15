/*
Write a JavaScript script that fetches and lists the title for all movies
by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
*/

const moviesList = document.querySelector("#list_movies");
const fetchMoviesBtn = document.querySelector("#fetch_movies");

fetchMoviesBtn.addEventListener("click", () => {
  getMovies();
});

async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    };
    const movies_json = await response.json();
    movies_json.results.forEach(movie => {
      movieTitle = movie["title"];
      if (movieTitle != undefined) {
        if (!validateMovieTitle(movieTitle)) {
          return;
        }
        try {
          moviesList.append(createMovieItem(movieTitle));
          console.log(`Movie created successfully: ${movieTitle}`);
        } catch (creationError) {
          console.warn(creationError);
        }
      }
    });
  } catch (error) {
    console.log(error.message);
  };
};

const createMovieItem = (movieTitle) => {
  newItem = document.createElement("li");
  newItem.textContent = movieTitle;
  return newItem;
}

const validateMovieTitle = (movieTitle) => {
  // Checks if the given movie already exists in any element of moviesList.
  if (Array.from(moviesList.querySelectorAll('li')).some(
      li => li.textContent === movieTitle
    )){
    console.warn(`Movie: ${movieTitle} Already exists`);
    return false;
  }
  return true;
}