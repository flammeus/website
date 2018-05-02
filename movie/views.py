import os
from django.shortcuts import render
from myweb.settings import MOVIES_PATH
from django.http import Http404
import pdb

def movie(request, url_directory=""):
    enable_previous = False
    if url_directory != None:
        enable_previous = True
    (result, found, abspath) = search(url_directory)
    path = "/play"+abspath.split("/movies")[1]
    
    return render(request, 'movie.html', {"list": result, "found": found, "path": path, "enable_previous": enable_previous})

def search(url_directory):
    if url_directory is None:
        url_directory = ""
    found = False
    result = ""
    abs_path = os.path.join(MOVIES_PATH, url_directory).rstrip('/')
    
    if os.path.isfile(abs_path) and abs_path.endswith(".webm"):
        found = True
    else:
        try:
            result = os.listdir(abs_path)
        except:
            raise Http404("Directory doesn't exit !")
    return (result, found, abs_path)
