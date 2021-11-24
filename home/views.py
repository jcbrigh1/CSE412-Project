from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        print("here 1")
        return render(request, 'index.html')
    if request.method == 'POST':
        print("here 2")
        if request.form['selection'] == 'name':
            print("here 3")
            return redirect('searchName')
    #return render(request, 'index.html')

def searchName(request):
    return render(request, 'searchName.html')

def search(request):
    return render(request, 'search.html')

def searchGenreStyle(request):
    return render(request, 'searchGenreStyle.html')

def searchPerson(request):
    return render(request, 'searchPerson.html')