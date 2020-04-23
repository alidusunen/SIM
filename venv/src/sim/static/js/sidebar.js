
$(function() {
    $('.ui.sidebar').sidebar('setting', 'dimPage', false);
    $('#toggler').click(function() {
      $('.sidebar').sidebar('toggle');
    });
});