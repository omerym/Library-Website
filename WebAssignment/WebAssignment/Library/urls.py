from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.About, name='about'),
    path('bookdetails/', views.BookDetails, name='bookDetails'),
    path('contactus/', views.ContactUs, name='contactUs'),
    path('editbook/', views.EditBook, name='editBook'),
    path('addbook/', views.AddBook, name='addBook'),
    path('editprofile/', views.EditProfile, name='editProfile'),
    path('login/', views.Login, name='Login'),
    path('register/', views.Register, name='register'),
    path('user/', views.UserProfile, name='user'),
    path('books/', views.GetBooks, name='GetBooks'),
    path('signout/', views.SignOut, name='SignOut'),
    path('books/borrowed/', views.GetBorrowedBooks, name='GetBorrowedBooks'),
    path('books/borrow/', views.Borrow, name='Borrow'),
    path('books/return/', views.Return, name='Return'),
    path('books/remove/', views.Remove, name='Remove'),

]

