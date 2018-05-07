from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^details/(\d+)',views.description,name='details'),
    url(r'^category/', views.category, name='classfied'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
