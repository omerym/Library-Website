function validatePassword(password, confirmedPassword) {
    if (password != null && confirmedPassword != null) {
        if (password.value == confirmedPassword.value) {
            confirmedPassword.setCustomValidity("");
        }
        else {
            confirmedPassword.setCustomValidity("wrong password");
        }
    }
}
pass = document.getElementById("password");
conPass = document.getElementById("confirmPassword");
if (pass != null && conPass != null) {
    pass.addEventListener("input", () => validatePassword(pass, conPass));
    conPass.addEventListener("input", () => validatePassword(pass, conPass));
}
function signout() {
    window.location.href = '/signout';
}