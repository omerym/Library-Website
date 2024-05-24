from django import forms


class BookForm(forms.Form):
    bookId = forms.CharField(label="id",max_length=50,required=True)
    title = forms.CharField(label="name",max_length=50,required=True)
    author = forms.CharField(label="author",max_length=50,required=True)
    category = forms.CharField(label="category",max_length=50,required=False)
    description = forms.CharField(label="description",max_length=255,required=False)

class UserForm(forms.Form):
    email = forms.CharField(label="email",max_length=50,required=True)
    username = forms.CharField(label="username",max_length=50,required=True)
    password = forms.CharField(label="password",max_length=50,required=True)
    currentuser = forms.CharField(label="currentuser",max_length=50,required=True)
