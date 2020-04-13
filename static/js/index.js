$(function () {
  displayRightForm();
  $('#profileType').change(displayRightForm);

  $('.mdb-select').materialSelect();
  $('.select-wrapper.md-form.md-outline input.select-dropdown').bind(
    'focus blur',
    function () {
      $(this).closest('.select-outline').find('label').toggleClass('active');
      $(this).closest('.select-outline').find('.caret').toggleClass('active');
    }
  );

  function displayRightForm() {
    if ($('#profileType').val() == 'stagiaire') {
      $('#aineForm').fadeOut(500, function () {
        $('#stagiaireForm').fadeIn(500);
      });
    } else {
      $('#stagiaireForm').fadeOut(500, function () {
        $('#aineForm').fadeIn(500);
      });
    }
  }

  // Material Select Initialization
  $('.multiple-select').materialSelect();

  $('#id_aine-username').removeAttr('autofocus');
  $('#id_aine-username').next().removeClass('active');
  $('#id_st-username').removeAttr('autofocus');
  $('#id_st-username').next().removeClass('active');
});
