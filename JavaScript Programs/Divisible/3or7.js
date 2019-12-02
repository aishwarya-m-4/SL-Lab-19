function isDiv() {

    var num = document.querySelector(".input").value;
    if (num % 3 == 0 && num % 7 == 0) {
        document.querySelector("h1").innerText = `${num} is divisible by both 3 and 7`;
    }
    else if (num % 3 == 0) {
        document.querySelector("h1").innerText = `${num} is divisible by 3`;
    }
    else if (num % 7 == 0) {
        document.querySelector("h1").innerText = `${num} is divisible by 7`;
    }
    else {
        document.querySelector("h1").innerText = `${num} is not divisible by 3 or 7`;
    }

}
