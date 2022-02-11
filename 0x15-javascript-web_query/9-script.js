$(
  $.get('https://fourtonfish.com/hellosalut/?lang=en',
    function (data) {
      $('#hello').text(data.hello);
    }));
