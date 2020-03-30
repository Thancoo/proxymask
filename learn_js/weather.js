$.ajax({
    type: 'GET',
    url:'https://www.tianqiapi.com/api/',
    data:'version=v1&city=贵阳',
    dataType: 'JSON',
    error: function () {
        alert('Error');
    },
    success: function (res) {
        console.log(res);
        let weather = document.getElementById('weather');
        weather.append('<li>City: ' + res.city + '</li>');
        weather.append('<li>Weather: ' + res.data[0].wea + '</li>');
        weather.append('<li>Tips: ' + res.data[0].air_tips + '</li>');
    }
});