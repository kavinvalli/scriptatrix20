AOS.init({
    duration: 1000
});

function stayTuned(e) {
    console.log("Stay Tuned Program Started")
    e.preventDefault();
    email = $('#form-email').val();
    console.log("Email For Adding: "+email)
    url = '/stay-tuned/' + email + '/';
    callApi(url, {}, "POST", function(data) {
        if (data != null) {
            $('#form-email').val('')
            var x = document.getElementById("snackbar");
            x.innerHTML = data.error_message
            x.className = "show";
            setTimeout(function() { x.className = x.className.replace("show", ""); }, 3000);
        }
        return false;
    })
};