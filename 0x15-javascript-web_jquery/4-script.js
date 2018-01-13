$(document).ready(() => {
  $('#toggle_header').click(() => {
    const className = $('header').attr('class');
    if (className === 'green') {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
