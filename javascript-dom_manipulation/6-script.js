//
const headcollector = document.querySelector('#character');

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    // Extrait le nom du personnage des données
    const characterName = data.name;
    // Définit le contenu texte de l'élément avec l'ID "character" avec le nom du personnage
    headcollector.textContent = characterName;
  });
