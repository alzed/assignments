const imdbId = window.location.search.substr(1)

async function fetchMovie(){
    let res = await fetch(`http://www.omdbapi.com/?i=${imdbId}&apikey=813bdc23&plot=full`);
    let data = await res.json();
    const movie = document.getElementById("movie");
    movie.innerHTML = `<section>
    <img src="${data.Poster}">
    <header>
        <h2>${data.Title}</h2>
        <h3>Rating: ${data.imdbRating}/10</h3>
        <h4>Genre: ${data.Genre}<br>
            Actors: ${data.Actors}<br>
            Language: ${data.Language}</h4>
        <p>${data.Plot}</p>
    </header>
</section>`;
}

