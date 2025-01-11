from django.shortcuts import render, redirect
from .models import Libro, Capitulo, Versiculo, Diccionario, Lectura, Tema, Autor, Division, Doctrina, Doct_texto, Doct_verso
from django.db.models import Q 
from django.db import connection
from django.db.models import Func
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline

# Create your views here.


########################   Biblia

def biblia(request):
    book = Libro.objects.all().order_by('id')
    return render(request, 'rv60app/biblia.html', {'books':book}) 

def chapter(request):
    chapter_select = request.GET.get('chapter_select') 
    book = Libro.objects.get(id=chapter_select) 
    #v = Versiculo.objects.raw(f"SELECT * FROM rv60app_versiculo WHERE id = {chapter_select};") 
    v = Versiculo.objects.filter(numero=chapter_select)
    for verse in v:
        print(verse.numero.caps_de_libros)


    if chapter_select: 
            chapters = Capitulo.objects.filter(libros_id=chapter_select) 
    else:
         chapters = None
    context = {
        'chapters': chapters,
        'book':book.libro_es
    }
   # return render(request, 'partials/chapter.html', context)
    return render(request, "index.html")    

########################   Home

def home(request):
    
      
      return render(request, 'rv60app/index.html')
  
########################   Dashboard
 
def dashboard(request):
      return render(request, 'rv60app/dashboard.html')  


########################   RV Lectura

def rvlectura(request):
    
      mi_lectura = Libro.objects.all().order_by('id')
      context = {'libros': mi_lectura}

      return render(request, 'rv60app/rvlectura.html', context=context)
  
########################   Doctrina

def doctrina(request):
    
      mi_lectura = Doctrina.objects.all().order_by('titulo')
      context = {'doctrinas': mi_lectura}

      return render(request, 'rv60app/doctrina.html', context=context)  
  
 ########################   Diccionario

def diccionario(request):
    
      mi_lectura = Diccionario.objects.all().order_by('palabra')
      context = {'diccionarios': mi_lectura}

      return render(request, 'rv60app/diccionario.html', context=context)   
  
 ########################   Diccionario

def tema(request):
    
      mi_lectura = Tema.objects.all().order_by('titulo')
      context = {'temas': mi_lectura}

      return render(request, 'rv60app/tema.html', context=context)     
