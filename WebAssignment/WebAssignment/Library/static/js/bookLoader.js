
class book {
    constructor(id, name, author,category=' ', description =' ') {
        this.id = id;
        this.name = name;
        this.author = author;
        this.category = category;
        this.description = description;
    }
}
function refresh() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        books = JSON.parse(this.response)
        var container = document.getElementById("books");
        container.innerHTML = '';
        for (book of books) {
            var span = document.createElement("span");
            span.innerHTML = getBookHtml(book);
            container.appendChild(span);
        }
    }
    xhttp.onerror = function () {
        var container = document.getElementById("books");
        container.innerHTML = 'failed to load books!';
    }
    xhttp.open("GET", "/books", true);
    xhttp.send();
    var container = document.getElementById("books");
    container.innerHTML = '<div class="book">Loading Books!</div>';
    document.getElementById("searchBar").value = "";
}
function loadBorrowedBooks() {
    var container = document.getElementById("books");
    container.innerHTML = '';
    for (book of getBorrowedBooks()) {
        var span = document.createElement("span");
        span.innerHTML = getBookHtml(book);
        container.appendChild(span);
    }
}
function returnBook() {
    const id = getId();
    x = JSON.parse(localStorage.getItem('borrowedBooks'));
    i = x.indexOf(id);
    x.splice(i, 1);
    localStorage.setItem('borrowedBooks', JSON.stringify(x));
}
function* getBorrowedBooks() {
    x = JSON.parse(localStorage.getItem('borrowedBooks'));
    books = JSON.parse(localStorage.getItem('books'));
    if (x == null || x.length == 0) {
        return [];
    }
    for (id of x) {
        book = books.find((b) => b.id == id);
        yield book;
    }
}
function getId() {
    const params = new URLSearchParams(document.location.search);
    const id = params.get("id");
    return id;
}
function remove() {

    const id = getId();
    books = JSON.parse(localStorage.getItem('books'));
    if (books == null || books.length == 0) return;
    for (i = 0; i < books.length; i++) {
        const b = books[i];
        if (b.id == id) {
            books.splice(i,1);
        }
    }
    localStorage.setItem('books', JSON.stringify(books));
    window.location.href = '.';
}
function goToEdit() {

    const id = getId();
    window.location.href = `/editbook?id=${id}`;
}
function borrow() {
    const id = getId();
    borrowedBooks = JSON.parse(localStorage.getItem('borrowedBooks'));
    if (borrowedBooks == null || borrowedBooks.length == 0) {
        borrowedBooks = [];
    }
    borrowedBooks.push(id);
    localStorage.setItem('borrowedBooks', JSON.stringify(borrowedBooks));
}
function getBookHtml(book) {
    return `<div onclick ="window.location.href='/bookdetails?id=${book.bookId}'" class="book">Title: ${book.title}<br />Author: ${book.author}<br /></div >`;
}
function toggleBorrowButon() {
    const id = getId();
    borrowedBooks = JSON.parse(localStorage.getItem('borrowedBooks'));
    if (borrowedBooks == null || borrowedBooks.length == 0 || borrowedBooks.indexOf(id) < 0) {
        document.getElementById('borrow').disabled = false;
        document.getElementById('return').disabled = true;
    }
    else {
        document.getElementById('borrow').disabled = true;
        document.getElementById('return').disabled = false;
    }
}
function search() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        books = JSON.parse(this.response)
        var container = document.getElementById("books");
        container.innerHTML = '';
        if (books.length == 0) {
            container.innerHTML = 'No books found!';
        }
        for (book of books) {
            var span = document.createElement("span");
            span.innerHTML = getBookHtml(book);
            container.appendChild(span);
        }
    }
    xhttp.onerror = function () {
        var container = document.getElementById("books");
        container.innerHTML = 'Failed to load books!';
    }
    searchBy = document.getElementById("search").value;
    query = document.getElementById("searchBar").value;
    xhttp.open("GET", `/books?${searchBy}=${query}`, true);
    xhttp.send();
    var container = document.getElementById("books");
    container.innerHTML = '<div class="book">Loading Books!</div>';
}
