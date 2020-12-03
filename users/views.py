from django.shortcuts import render,redirect

# Create your views here.

from users.forms import RecipeRegistrationForm

# username:jessy
# password:Jessy12345

def registration(request):
    form=RecipeRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RecipeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"users/login.html",context)
        else:
            context["form"]=form
            return render(request,"users/register.html",context)
    else:
        return render(request,"users/register.html",context)

# def login(request):
