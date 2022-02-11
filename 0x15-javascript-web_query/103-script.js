'use strict';
$(() => {
  const getHello = () => {
    const code = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${code}`,
      (data) => {
        $('#hello').text(data.hello);
      });
  };

  $('#btn_translate').click(getHello);
  $('#language_code').keydown((event) => {
    if (event.key === 'Enter') { getHello(); }
  });
});
