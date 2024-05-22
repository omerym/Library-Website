from os import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages

from WebAssignment.Library.models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    template = loader.get_template('landingPage.html')
    return HttpResponse(template.render())
def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())
def AddBook(request):
    messages.info(request,"");
    if request.method == "POST":   
        form = BookForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            if(Book.objects.filter(bookId = d['bookId'])):
                messages.error(request, f"book with id {d['bookId']} already exists!")
                return render(request,"AddBookPage.html", {"form": form})
            else:
                b = Book(bookId = d['bookId'], title = d['title'], author = d['author'], catogery = d['catogery'] ,description = d['description'])
                b.save()
                return HttpResponseRedirect(f"/bookdetails?id={form.cleaned_data['bookId']}")
    else:
        form = BookForm()
        return render(request,"AddBookPage.html", {"form": form})
def BookDetails(request):
    template = loader.get_template('BookDetails.html')
    return HttpResponse(template.render())
def ContactUs(request):
    template = loader.get_template('ContactUs.html')
    return HttpResponse(template.render())
def EditBook(request):
    template = loader.get_template('EditBookPage.html')
    return HttpResponse(template.render())
def EditProfile(request):
    template = loader.get_template('EditProfile.html')
    return HttpResponse(template.render())
def User(request):
    template = loader.get_template('UserProfile.html')
    return HttpResponse(template.render())
def Login(request):
    template = loader.get_template('LoginPage.html')
    return HttpResponse(template.render())
def Register(request):
    template = loader.get_template('RegisterPage.html')
    return HttpResponse(template.render())