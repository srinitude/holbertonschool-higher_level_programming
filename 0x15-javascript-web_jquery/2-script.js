document.addEventListener('DOMContentLoaded', (event) => {
  const redHeader = document.getElementById('red_header');
  redHeader.addEventListener('click', (event) => {
    const header = document.getElementsByTagName('header')[0];
    header.style.color = '#FF0000';
  });
});
