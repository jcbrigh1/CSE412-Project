from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        if request.POST['selection'] == 'name':
            return redirect('searchName/')
        elif request.POST['selection'] == 'person':
            return redirect('searchPerson/')
        elif request.POST['selection'] == 'genreStyle':
            return redirect('searchGenreStyle/')
    #return render(request, 'index.html')

def searchName(request):
    return render(request, 'searchName.html')
    

def searchGenreStyle(request):
    return render(request, 'searchGenreStyle.html')

def searchPerson(request):
    return render(request, 'searchPerson.html')