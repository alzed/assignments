const btn = document.getElementById('searchbtn');
btn.addEventListener('click', function (event) {
    find();
    event.preventDefault();
  });

const card = ` <div class="card">
<img src="img_snowtops.jpg" alt="Alps">
<div class="container center">
  <p>The Italian / Austrian Alps</p>
</div>
</div> `;

async function find(){
    console.log('search');
    let keyword = document.getElementById('search').value;
    let res = await fetch(`http://www.omdbapi.com/?i=tt3896198&apikey=813bdc23&s=${keyword}`);
    let data = await res.json();
    let result = document.getElementById('result');
    result.innerHTML = JSON.stringify(data);
    console.log(data);
    return false
}


