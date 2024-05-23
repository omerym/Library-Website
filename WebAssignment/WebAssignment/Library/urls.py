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

    path('delete_book/<str:book_id>/', views.deleteBook, name='deleteBook'),
    path('borrow_book/<str:book_id>/', views.deleteBook, name='borrow_book'),
    path('return_book/<str:book_id>/', views.deleteBook, name='return_book'),
    path('Userprofile/', views.Userprofile, name='Userprofile'),

]

