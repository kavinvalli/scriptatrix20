AOS.init({
    duration: 1000
});

function stayTuned(e) {
    console.log("Stay Tuned Program Started")
    e.preventDefault();
    email = $('#form-email').val();
    console.log("Email For Adding: " + email)
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

for (let a of document.querySelectorAll('.dot-nav ul li a')) {
    a.addEventListener('click', e => {
        e.preventDefault();
        document.querySelector('#' + e.target.parentNode.href.split('#')[1]).scrollIntoView({ behavior: 'smooth' });
    });
}

window.onscroll = function() { myFunction() };

var navbar = document.getElementById("navbar");

function myFunction() {
    if (window.pageYOffset > window.innerHeight) {
        navbar.classList.add("fixed-top");
        $('body').css('padding-top', $('.navbar').outerHeight() + 'px');
    } else {
        navbar.classList.remove("fixed-top");
        $('body').css('padding-top', '0');
    }
}

document.addEventListener('DOMContentLoaded', () => {

    const themeStylesheet = document.getElementById('theme');
    const storedTheme = localStorage.getItem('theme');
    const storedText = localStorage.getItem('text');
    const storedSrc = localStorage.getItem('src');
    const themeToggle = document.getElementById('theme-toggle');
    const storedBanner = localStorage.getItem('bannerSrc')
    if(storedTheme){
        themeStylesheet.href = storedTheme;
    }
    if(storedText){
        themeToggle.innerHTML = storedText;
    }
    if(storedSrc) {
        $('#devices-image').attr('src', storedSrc)
    }
    if(storedBanner) {
        $('#banner-image').attr('src', storedBanner)
    }
    const devices = document.getElementById('#devices-image')
    themeToggle.addEventListener('click', () => {
        // if it's light -> go dark
        if(themeStylesheet.href.includes('light')){
            themeStylesheet.href = "../../../static/core/css/index-dark.css";
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
            $('#devices-image').attr('src', '../../../static/core/img/device/dark/2x/devices.png')
            $('#banner-image').attr('src', '../../../static/core/img/1x/banner-dark.png')
            localStorage.setItem('theme', "../../../static/core/css/index-dark.css");
            localStorage.setItem('text','<i class="fas fa-sun"></i>')
            localStorage.setItem('src', '../../../static/core/img/device/dark/2x/devices.png')
            localStorage.setItem('bannerSrc', '../../../static/core/img/1x/banner-dark.png')
        } else {
            themeStylesheet.href = "../../../static/core/css/index-light.css";
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
            $('#devices-image').attr('src', '../../../static/core/img/device/2x/devices.png')
            $('#banner-image').attr('src', '../../../static/core/img/19787.jpg')
            localStorage.setItem('theme', "../../../static/core/css/index-light.css");
            localStorage.setItem('text','<i class="fas fa-moon"></i>')
            localStorage.setItem('src', '../../../static/core/img/device/2x/devices.png')
            localStorage.setItem('bannerSrc', '../../../static/core/img/19787.jpg')
        }
    })
})