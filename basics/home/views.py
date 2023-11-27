from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("""<h1> Supp Bois! </h1>
#                             <p> Coming from a Django Server </p>
#                             <hr>
#                             <h3 style="color:red"> Aight Everyone! </h3>
#                         """)

def home(request):
    
    peoples = [
        {'name': 'John', 'age': 18},
        {'name': 'Petrucci', 'age': 28},
        {'name': 'Mike', 'age': 30},
        {'name': 'Magini', 'age': 14},
        {'name': 'James', 'age': 36},
    ]
    
    return render(request, 'home/index.html', context={'peoples': peoples})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Page reload was successful </h1>")