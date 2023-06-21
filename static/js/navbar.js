const dropdown = document.querySelector('.dropdown-container');
const image = document.querySelector('.nav-profile-image');

function toggleMenu() {
  console.log('Working');
  dropdown.classList.toggle('open-menu');
}


image.addEventListener('click',toggleMenu);
