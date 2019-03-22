$(function() {
    $('.professions').hide();
    $('#profession').change(function(){
      $('.professions').hide();
      $('#' + $(this).val()).show();
    });
  });