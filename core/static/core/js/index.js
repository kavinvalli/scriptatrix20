$(document).ready(function() {
    $(window).bind('scroll', function() {
        var headerHeight = $('.flex').height();
        if ($(window).scrollTop() > headerHeight) {
            $('.nav-bar').addClass('fixed');
            $('.nav-1').addClass('toleft');
        } else {
            $('.nav-bar').removeClass('fixed');
            $('.nav-1').removeClass('toleft');
        }
    });
});

const loadingAnimationTime = 2000

const showMainAnimation = (parent) => {
    const boxContainer = document.createElement("div");
    boxContainer.style.overflow = "hidden";
    const box = document.createElement("div");
    box.classList.add("box", "flex");
    parent.appendChild(boxContainer);
    boxContainer.appendChild(box);
    const quote = ["Make", "Life", "Simple", "with", "__________"];
    let delay = 0;
    for (let word in quote) {
        let text = document.createElement("span");
        text.textContent = quote[word];
        text.classList.add("animate-slideup");
        delay = delay + 22;
        text.style.animationDelay = delay + "ms";
        box.appendChild(text);
    }
    const lastAnimationTime = 1000 + delay;
    let text = document.createElement("div");
    text.classList.add("fs", "flex");
    text.style.animationDelay = lastAnimationTime - 100 + "ms";
    box.appendChild(text);
};

const revealCurtain = (parent) => {
    const curtain = document.createElement("div");
    curtain.classList.add("flex", "curtain");
    parent.appendChild(curtain);
    const progressBar = document.createElement("div");
    progressBar.classList.add("progressBar");
    curtain.appendChild(progressBar);
    progressBar.classList.add("progressGrow-animation");
    return curtain;
};

const init = () => {
    const container = document.getElementById("main");
    const curtain = revealCurtain(container);
    setTimeout(() => {
        container.removeChild(curtain);
        showMainAnimation(container);
    }, loadingAnimationTime + 100)
};

init();