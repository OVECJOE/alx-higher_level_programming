$(function () {
  $('#btn_translate').click(() => {
    const code = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${code}`,
      (data) => {
        $('#hello').text(data.hello);
      });
  });
});
