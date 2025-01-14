from django.shortcuts import render
from rv60app.models import Libro , Capitulo, Versiculo



def menu(request):
    book = Libro.objects.all()
    return render(request, 'menu/menu.html', {'books':book}) 

def chapter(request):
    chapter_select = request.GET.get('chapter_select') 
    book = Libro.objects.get(id=chapter_select)  
    v = Versiculo.objects.filter(capitulos=chapter_select)  
    if chapter_select: 
            chapters = Capitulo.objects.filter(libros=chapter_select) 
 
    else:
         chapters = None
    context = {
        'chapters': chapters,
        'book':book.libro_es
    }
    return render(request, 'menu/partials/chapter.html', context)

def verse(request):
    verse_select = request.GET.get('verse_select') 
    if verse_select:
         verses = Versiculo.objects.filter(capitulos=verse_select)
    else:
         verses = None
    context = {
         "verses":verses,
    }
    return render(request, "menu/partials/verse.html", context)