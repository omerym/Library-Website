import email
from mimetypes import encodings_map
from os import name
import re
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.http import JsonResponse
from WebAssignment.Library.models import Book
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from .forms import BookForm

from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "landingPage.html")

def SignOut(request):
    logout(request)
    return redirect('/')
        
def About(request):
    return render(request, "About.html")

def AddBook(request):
    if request.method == "POST":   
        form = BookForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            if(Book.objects.filter(bookId = d['bookId'])):
                messages.error(request, f"book with id {d['bookId']} already exists!")
                return render(request,"AddBookPage.html", {"form": form})
            else:
                b = Book(bookId = d['bookId'], title = d['title'], author = d['author'], category = d['category'] ,description = d['description'])
                b.save()
                return HttpResponseRedirect(f"/bookdetails?id={form.cleaned_data['bookId']}")
    else:
        form = BookForm()
        return render(request,"AddBookPage.html", {"form": form})
    template = loader.get_template('AddBookPage.html')
    return HttpResponse(template.render())

def BookDetails(request):
    book = Book.objects.filter(bookId = request.GET["id"])
    if book:
        return render(request,"BookDetails.html",{"book":book.first(),"id":book.first().bookId})
    return render(request,"BookDetails.html",{"book":None,"id":request.GET["id"]})

def ContactUs(request):
    template = loader.get_template('ContactUs.html')
    return HttpResponse(template.render())

def EditBook(request):
    template = loader.get_template('EditBookPage.html')
    return HttpResponse(template.render())

def EditProfile(request):
    template = loader.get_template('EditProfile.html')
    return HttpResponse(template.render())

def UserProfile(request):
    template = loader.get_template('UserProfile.html')
    return HttpResponse(template.render())

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'loginPage.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        userType = request.POST.get('userType')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        user = User.objects.create_user(
            username=username,
            email= email
        )
        user.set_password(password)
        if userType == 'Admin':
            user.user_permissions.add(GetAdminPermission())
        user.save() 
        messages.info(request, "Account created Successfully!")
        return redirect('/login/')
    return render(request,"RegisterPage.html")
def GetBooks(request):
    get = request.GET
    if get.get("title",None):
        return GetBooksByTitle(request)
    if get.get("author",None):
        return GetBooksByAuthor(request)
    if get.get("category",None):
        return GetBooksByCategory(request)
    return GetAllBooks(request)
def GetAllBooks(request):
    data = Book.objects.all().values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)
def GetBooksByTitle(request):
    title = request.GET["title"]
    print(title)
    data = Book.objects.filter(title__icontains=title).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)    
def GetBooksByCategory(request):
    cat = request.GET["category"]
    print(cat)
    data = Book.objects.filter(category__icontains=cat).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)    
def GetBooksByAuthor(request):
    author = request.GET["author"]
    print(author)
    data = Book.objects.filter(author__icontains=author).values().iterator()
    data = Book.objects.all().values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)

def GetAdminPermission():
    p = Permission.objects.filter(codename='admin').first()
    if p == None:
        c = ContentType.objects.get_for_model(Book)
        p = Permission.objects.create(codename = 'admin', content_type = c)
        p.save()
    return p