function reload() {
    type = sessionStorage.getItem('usertype');
    var all = document.getElementsByTagName("*");
    for (x of all) {
        x.style.display = '';
    }
    if (type != 'User' && type != 'Admin') {
        u = document.getElementsByName("any");
        for (x of u) {
            x.style.display = 'none';
        }
    }
    if (type != 'User') {
        u = document.getElementsByName("User");
        for (x of u) {
            x.style.display = 'none';
        }
    }
    if (type != 'Admin') {
        u = document.getElementsByName("Admin");
        for (x of u) {
            x.style.display = 'none';
        }
    }
    if (type != null) {
        u = document.getElementsByName("unsigned");
        for (x of u) {
            x.style.display = 'none';
        }
    }
}
function signout() {
    sessionStorage.removeItem('username');
    sessionStorage.removeItem('usertype');
    reload();
}
reload();