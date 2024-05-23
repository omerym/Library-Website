from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    template = loader.get_template('landingPage.html')
    return HttpResponse(template.render())

def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def AddBook(request):
    template = loader.get_template('AddBookPage.html')
    return HttpResponse(template.render())

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

def bookDetails(request):
    book =  get_object_or_404(Book, id=book_id)
    user_type = 'unsign'
    if request.user.is_authenticated:
        if request.user.is_superuser:
            user_type = 'Admin'
        else:
            user_type = 'User'
    return render(request,'BookDetails.html',{'book':book,'user_type':user_type})