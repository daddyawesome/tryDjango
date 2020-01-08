from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args, **kwargs
    my_context = {
        "my_text" : "This is About Us",
        "my_number" : 9166190483,
        "my_list" : [123, 456, 789 ,'abc']

    }
    return render(request, "about.html", my_context)

def social_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Social Page</h1>")