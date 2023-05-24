from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name = "starting-page"),
    path('post', views.post, name = "post"),
    path('post/<slug:slug>', views.post_slug, name = "post-slug")
]
