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

class MailForm(forms.Form):
    email = forms.CharField(label="email",max_length=50,required=True)
    message = forms.CharField(label="message",max_length=200,required=True)
    phone = forms.CharField(label="phone",max_length=50,required=True)
    first_name = forms.CharField(label="first_name",max_length=50,required=True)
    last_name = forms.CharField(label="last_name",max_length=50,required=True)
