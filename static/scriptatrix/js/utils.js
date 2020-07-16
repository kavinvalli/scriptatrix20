function callApi(url, body, method, callback) {
    console.log(typeof body)
    var token = $('input[name="csrfmiddlewaretoken"').attr('value');
    if (method == "POST") {
        $.ajax({
            url: url,
            method: "POST",
            dataType: 'json',
            headers: {
                'X-CSRFToken': token,
            },
            data: body,
            success: function(data) {
                callback(data);
            },
            error: function(xhr, status, error) {
                console.log('error')
                alert('There was some Error. Please Try Again.')
            }
        });
    } else {
        $.ajax({
            url: url,
            dataType: 'json',
            success: function(data) {
                callback(data);
            }
        });
    }
}