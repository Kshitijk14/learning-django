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
    
    text = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    
    vegetables = ['tomato', 'potato', 'cucumber', 'bell pepper']
    
    return render(request, 'home/index.html', context={'page': 'Django Babies', 'peoples': peoples, 'text': text, 'vegetables': vegetables})


def about(request):
    context = {'page': 'About'}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {'page': 'Contact'}
    return render(request, 'home/contact.html', context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Page reload was successful </h1>")