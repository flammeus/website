from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from movie import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^pacman$', TemplateView.as_view(template_name='pacman.html'), name='pacman'),
	url(r'^snake$', TemplateView.as_view(template_name='snake.html'), name='snake'),
	url(r'^space_invader$', TemplateView.as_view(template_name='space_invader.html'), name='space_invader'),
	url(r'^movie/(?P<url_directory>[a-zA-Z0-9\-\/_\.]*/)?$', views.movie, name='movie'),
]
