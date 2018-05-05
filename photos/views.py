from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')
def index(request):
    photos=Gallery.objects.all()
    return render(request,'index.html',{"photo": photo})
