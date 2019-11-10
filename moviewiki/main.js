let page = 1;
let result = document.getElementById('result');

const moreBtn = document.getElementById('showmore');

if (result.innerHTML === ""){
    moreBtn.style.display = "none"
}

const btn = document.getElementById('searchbtn');
btn.addEventListener('click', function (event) {
    find();
    event.preventDefault();
});

async function find() {
    console.log('search');
    let keyword = document.getElementById('search').value;
    let res = await fetch(`https://www.omdbapi.com/?i=tt3896198&apikey=813bdc23&s=${keyword}&page=${page}`);
    let data = await res.json();
    let result = document.getElementById('result');
    result.innerHTML = createResult(data);
    moreBtn.style.display = "block";
}

function createResult(data) {
    let card = " ";
    console.log(data);
    data.Search.forEach((movie) => {
        card += `<a href="/movie.html?${movie.imdbID}"> <div class="card" id="${movie.imdbID}">
        <img src="${movie.Poster}" id="${movie.imdbID}" alt="${movie.Title}">
        <div class="container center">
          <p>${movie.Title}</p>
        </div>
        </div> </a>`        
    });
    return card;
}

moreBtn.addEventListener('click', function (event) {
    showMore();
    event.preventDefault();
});

async function showMore(){
    let keyword = document.getElementById('search').value;
    page += 1;
    let res = await fetch(`https://www.omdbapi.com/?i=tt3896198&apikey=813bdc23&s=${keyword}&page=${page}`);
    let data = await res.json();
    let result = document.getElementById('result');
    result.innerHTML += createResult(data);
    console.log(data);
}
