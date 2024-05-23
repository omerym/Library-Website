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
    if not request.user.is_authenticated or not request.user.has_perm('Library.admin'):
        redirect('/')
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
                return redirect(f"/bookdetails?id={form.cleaned_data['bookId']}")
    else:
        form = BookForm()
        return render(request,"AddBookPage.html", {"form": form})
    return render(request,"AddBookPage.html")
def BookDetails(request):
    book = Book.objects.filter(bookId = request.GET["id"])
    if book:
        return render(request,"BookDetails.html",{"book":book.first(),"id":book.first().bookId})
    return render(request,"BookDetails.html",{"book":None,"id":request.GET["id"]})

def ContactUs(request):
    return render(request,'ContactUs.html')

def EditBook(request):
    if not request.user.is_authenticated or not request.user.has_perm('Library.admin'):
        redirect('/')
    if request.method == "POST":
        #BookID=request.GET.get('id')
        #print(f"BookID: {BookID}")
        #if not BookID:
            #redirect('/')
        #else:
            form = BookForm(request.POST)
            
            
            if form.is_valid():
                FormData = form.cleaned_data
                CurrentBook = Book.objects.get(bookId=FormData['bookId'])
                if(Book.objects.filter(bookId=FormData['bookId'])):
                    print(f"BookID: {FormData['bookId']}")
                    CurrentBook.title= FormData['title']
                    CurrentBook.author=FormData['author']
                    CurrentBook.category=FormData['category']
                    CurrentBook.description=FormData['description']
                    CurrentBook.save()
                    return redirect(f"/bookdetails?id={form.cleaned_data['bookId']}")
            else:
                messages.error(request, f"book does not exist")
                return render(request,"EditBookPage.html", {"form": form})
                
    else:
        form = BookForm()
        return render(request,"EditBookPage.html", {"form": form})
    template = loader.get_template('EditBookPage.html')
    return HttpResponse(template.render())

def EditProfile(request):
    if not request.user.is_authenticated:
        redirect('/')
    return render(request,'EditProfile.html')

def UserProfile(request):
    if not request.user.is_authenticated:
        redirect('/')
    return render(request,'UserProfile.html')

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

def GetBorrowedBooks(request):
    if not request.user.is_authenticated:
        return JsonResponse(None, safe = False)
    data = Book.objects.filter(borrowedBy = request.user).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)
    

def GetAllBooks(request):
    data = Book.objects.all().values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)
def GetBooksByTitle(request):
    title = request.GET["title"]
    data = Book.objects.filter(title__icontains=title).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)    
def GetBooksByCategory(request):
    cat = request.GET["category"]
    data = Book.objects.filter(category__icontains=cat).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)    
def GetBooksByAuthor(request):
    author = request.GET["author"]
    data = Book.objects.filter(author__icontains=author).values().iterator()
    x=[]
    for i in data:
        x.append(i)
    return JsonResponse(x, safe = False)

def Borrow(request):
    id = request.GET.get("id",None)
    book = Book.objects.filter(bookId = id).first()
    if not id or not request.user.is_authenticated or not book or book.borrowedBy:
        return redirect('/')
    book.borrowedBy = request.user
    book.save()
    return redirect(f'/bookdetails?id={id}')
 
def Return(request):
    id = request.GET.get("id",None)
    book = Book.objects.filter(bookId = id).first()
    if not id or not request.user.is_authenticated or not book or book.borrowedBy != request.user:
        return redirect('/')
    book.borrowedBy = None
    book.save()
    return redirect(f'/bookdetails?id={id}')

def Remove(request):
    id = request.GET.get("id",None)
    book = Book.objects.filter(bookId = id)
    if request.user.has_perm('Library.admin') and  id and book:
        book.delete()
    return redirect('/')

def GetAdminPermission():
    p = Permission.objects.filter(codename='admin').first()
    if p == None:
        c = ContentType.objects.get_for_model(Book)
        p = Permission.objects.create(codename = 'admin', content_type = c)
        p.save()
    return p