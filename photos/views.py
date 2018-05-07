from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery,Location,Category
# Create your views here.

def index(request):


    photo=Gallery.objects.all()

    return render(request,'index.html',{"photo": photo })

def search_results(request):

    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get("category")
        searched_categories=Gallery.search_by_category(search_term)
        message=f"{search_term}"


        return render(request, 'all-temps/search.html',{"message":message, "categories": searched_categories})

    else:
        message="you haven't searched for any category"
        return render(request,'all-temps/search.html',{"massage":message})

def description(request,id):

    try:
        picture=Gallery.objects.get(id=id)
    except Gallery.DoesNotExist:
        raise Http404()

    return render(request,'all-temps/picture.html', {"picture": picture})


def category(request):

    return
