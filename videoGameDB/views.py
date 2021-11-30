from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def dictfetchall(cursor):
    "this function is copied from Django's documentation"
    "Returns all the rows from cursor as a dict"
    "needed since we are dealing with raw queries"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


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
    name_term = ''

    if 'q' in request.GET:
        name_term = request.GET['q']

    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Videogame WHERE name = %s", [name_term])
        res = dictfetchall(cursor)
    
    if len(res) > 0:
        #print(res);
        videogame = {'videogame' : res}
        return render(request, 'searchName.html', videogame)
    else:
        return render(request, 'searchName.html')
    

def searchGenreStyle(request):
    genre = ''

    if 'q' in request.GET:
        genre = request.GET['q']

    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Videogame WHERE genre = %s", [genre])
        res = dictfetchall(cursor)

    if len(res) > 0:
        videogame = {'videogame' : res}
        return render(request, 'searchGenreStyle.html', videogame)
    else:
        return render(request, 'searchGenreStyle.html')


def searchPerson(request):
    p_name = ''

    if 'q' in request.GET:
        p_name = request.GET['q']

    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Person WHERE name = %s", [p_name])
        res = dictfetchall(cursor)

    if len(res) > 0:
        videogame = {'videogame' : res}
        return render(request, 'searchPerson.html', videogame)
    else:
        return render(request, 'searchPerson.html')

    return render(request, 'searchPerson.html')
