$(document).ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(() => {
    $('.my_list li:last-child').remove();
  });
  $('#clear_list').click(() => {
    $('.my_list > li').remove();
  });
});
