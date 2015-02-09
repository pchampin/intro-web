// jshint browser:true, devel:true

function button_click(evt) {
    var input = document.getElementsByTagName("input")[0];
    var key = evt.target.textContent;
    if (key === "×" || key === "x") {
        key = "*";
    } else if (key === "÷") {
        key = "/";
    } else if (key === "←" || key === "&lt;-") {
        key = "<-";
    }

    if (key === "<-") {
        input.value = input.value.substr(0, input.value.length-1);
        if (input.value === "") {
            input.value = "0";
        }
    } else if (key === "=") {
        try {
            input.value = eval(input.value);
        }
        catch (ex) {
            input.value = "err";
        }
    } else {
        if (input.value === "0" || input.value === "err") {
            input.value = "";
        }
        input.value += key;
    }
}

window.addEventListener("load", function(evt) {
    var buttons = document.getElementsByTagName("button");
    for(var i=0; i<buttons.length; i+=1) {
        buttons[i].addEventListener("click", button_click);
    }
});

console.log("calculette.js loaded");
