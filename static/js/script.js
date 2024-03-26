$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
});


/* Code for toggling password visibility, adapted from W3Schools */
function togglePasswordVisibility() {
    var passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}
