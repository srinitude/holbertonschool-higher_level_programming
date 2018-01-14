$(document).ready(() => {
  $('#btn_search').click((event) => {
    const cityName = $('#city_search').val();
    $.ajax({
      type: 'GET',
      url: `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22${cityName}%22)&format=json`,
      dataType: 'json',
      encode: true
    })
      .done((data) => {
        const windSpeed = data.query.results.channel.wind.speed;
        $('#wind_speed').text(windSpeed);
      });
    event.preventDefault();
  });
});
