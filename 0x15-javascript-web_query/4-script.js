$('#toggle_header').click(
  function () {
    if ($('header').attr('class') === 'red') { $('header').removeClass('red').addClass('green'); } else { $('header').removeClass('green').addClass('red'); }
  });
