document.addEventListener('DOMContentLoaded', function () {
  // Sélectionne un élément HTML avec l'ID "hello" et stocke-le dans la variable "headcollector"
  const headcollector = document.querySelector('#hello');

  // Définit l'URL de l'API à partir de laquelle nous allons récupérer les données
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Utilise la fonction fetch pour effectuer une requête HTTP GET vers l'URL spécifiée
  fetch(url)
    .then(response => {
    // Le callback .then est exécuté lorsque la réponse de la requête est reçue
    // Convertit la réponse en format JSON et la renvoie en tant que nouvelle promesse
      return response.json();
    })
    .then(data => {
    // Le callback .then est exécuté lorsque les données JSON sont disponibles
    // Extrait la valeur de "hello" de l'objet "data" et la stocke dans la variable "datalist"
      const datalist = data.hello;
      // Utilise la méthode textContent pour définir le contenu texte de l'élément "headcollector"
      headcollector.textContent = datalist;
    });
});
