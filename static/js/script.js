document.getElementById("demoImg").addEventListener("mouseover", ImgDemo);

function ImgDemo() {
    alert("Hello!");
}

function enlarge(x) {
    x.style.height = "80%";
    x.style.width = "80%";
    x.style.textSelf = "center";
}