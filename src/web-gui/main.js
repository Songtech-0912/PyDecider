
// Javascript runs Python mainFunction() when button is pushed

function js_startPython() {
    eel.mainFunction();    // calls the Python function from Javascript
}

// Python calls on either yesFunction() or noFunction() depending on python result

eel.expose(yesFunction); // Expose this function to Python
function yesFunction() {
    location.href='result-yes.html'
}

eel.expose(noFunction); // Expose this function to Python
function noFunction() {
    location.href='result-no.html'
}

// Loader animation effect

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("content").style.display = "block";
}

// Go back button

function backFunction() {
    location.href='index.html';
}