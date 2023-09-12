// Sélectionne un élément HTML avec l'ID "list_movies" et stocke-le dans la variable "headcollector"
const headcollector = document.querySelector('#list_movies');

// Définit l'URL de l'API à partir de laquelle nous allons récupérer les données des films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Utilise la fonction fetch pour effectuer une requête HTTP GET vers l'URL spécifiée
fetch(url)
  .then(response => {
    // Le callback .then est exécuté lorsque la réponse de la requête est reçue
    // Convertit la réponse en format JSON et la renvoie en tant que nouvelle promesse
    return response.json();
  })
  .then(data => {
    // Le callback .then est exécuté lorsque les données JSON sont disponibles
    // Extrait la liste de films de l'objet "data" et la stocke dans la variable "dataList"
    const dataList = data.results;

    // Crée un élément HTML <ul> (liste non ordonnée) pour afficher les titres des films
    const ul = document.createElement('ul');

    // Parcours la liste de films "dataList" en utilisant forEach pour itérer sur chaque film
    dataList.forEach(movie => {
      // Crée un élément HTML <li> (élément de liste) pour chaque film
      const li = document.createElement('li');

      // Définit le contenu texte de l'élément <li> avec le titre du film actuel
      li.textContent = movie.title;

      // Ajoute l'élément <li> à la liste non ordonnée (<ul>)
      ul.appendChild(li);
    });

    // Ajoute la liste de films (<ul>) à l'élément HTML avec l'ID "list_movies"
    headcollector.appendChild(ul);
  })

