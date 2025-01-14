from django.shortcuts import render, redirect
from rv60app.models import Libro, Capitulo, Versiculo
from django.db.models import Q 
from django.db import connection
from django.db.models import Func
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline



class Unaccent(Func):
    function = 'unaccent'
    template = "%(function)s(%(expressions)s)"

def unaccent_string(value):
    """Helper function to unaccent a string using raw SQL."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT unaccent(%s);", [value])
        return cursor.fetchone()[0]


def search(request):  
    choice = request.GET.get('choice') 
    if choice:
        return render(request, "search/partials/results.html", {'choice':choice})
    return render(request, "search/search.html")


def results(request):
    choice = request.GET.get('choice').strip()
    c = unaccent_string(choice)
    vector = SearchVector(Unaccent('contenido'))
    query = SearchQuery(c)
    search_headline = SearchHeadline('contenido',query) 
    
    verse = Versiculo.objects.annotate(search=vector).annotate(headline=search_headline).filter(search=c) 

    context = {
        'verse':verse, 
        'count':verse.count()
    }
    return render(request, "search/partials/results.html", context)


def get_chapter(request, book, chapter):
    book_by_chapter = Libro.objects.get(libro_es=book)
    chapter_by_chapter = Capitulo.objects.get(libros=book_by_chapter, caps_de_libros=chapter)
    verse_by_chapter = Versiculo.objects.filter(capitulos=chapter_by_chapter) 
    all_chapter = Capitulo.objects.filter(libros=book_by_chapter) 
    print(all_chapter.count()) 
    
    prev = request.POST.get('prev')
    next = request.POST.get('next') 
    new_book_value = Libro.objects.get(id=book_by_chapter.id) 
    num = all_chapter.count() 
    num2 = all_chapter.count() 
    
    if request.method == "POST": 
        if prev == 'prev': 
            num = int(chapter)-1
            print(f'number calculated for', num)   
            if num <= 0:
                new_book_value1 = Libro.objects.get(id=new_book_value.id-1) #gets book count for previous book
                new_chapter_value1 = Capitulo.objects.filter(libros=new_book_value1).count()#gets chapter count for previous chapter
                return redirect('get_chapter',new_book_value1.libro_es,new_chapter_value1)
            return redirect('get_chapter',book_by_chapter.libro_es,chapter_by_chapter.caps_de_libros-1)
        if next == 'next':
            num =+ int(chapter)+1
            print(f'number calculated for', num) 
            if num > num2:
                new_book_value1 = Libro.objects.get(id=new_book_value.id+1) #gets book count for previous book
                return redirect('get_chapter',new_book_value1.libro_es,1)
            return redirect('get_chapter',book_by_chapter.libro_es,chapter_by_chapter.caps_de_libros+1)

    context = {
        "contenido":verse_by_chapter,
        'book':book_by_chapter,
        'chapter':chapter_by_chapter,

    }
    return render(request, "search/get-chapter.html", context)