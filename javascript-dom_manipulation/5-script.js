const clickupdateheader = document.querySelector('#update_header');
const header = document.querySelector('header');

clickupdateheader.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
