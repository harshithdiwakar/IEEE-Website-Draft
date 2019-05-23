from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('committee', views.committee, name = 'committee'),
    path('news',views.news, name = 'news'),
    path('events', views.events, name = 'events'),
    path('about', views.about, name = 'about'),
    path('excom', views.excom, name = 'excom'),
    path('posts', views.posts, name = 'posts'),
    path('gallery', views.gallery, name = 'gallery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)