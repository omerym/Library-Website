
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
    xhttp.open("GET", "/books/borrowed", true);
    xhttp.send();
    var container = document.getElementById("books");
    container.innerHTML = '<div class="book">Loading Books!</div>';
}
function returnBook() {
    const id = getId();
    window.location.href = `/books/return?id=${id}`;
}
function getId() {
    const params = new URLSearchParams(document.location.search);
    const id = params.get("id");
    return id;
}
function remove() {

    const id = getId();
    window.location.href = `/books/remove?id=${id}`;
}
function goToEdit() {

    const id = getId();
    window.location.href = `/editbook?id=${id}`;
}
function borrow() {
    const id = getId();
    window.location.href = `/books/borrow?id=${id}`;
}
function getBookHtml(book) {
    return `<div onclick ="window.location.href='/bookdetails?id=${book.bookId}'" class="book">Title: ${book.title}<br />Author: ${book.author}<br /></div >`;
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
