from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name = "starting-page"),
    path('post', views.post, name = "post"),
    path('add', views.add, name = "add"),
    path('adddata', views.adddata, name = "adddata"),
    
    path('post/<slug:slug>', views.post_slug, name = "post-slug")
]
