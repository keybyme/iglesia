from django.db.models import F
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
      busca_doctrina=request.GET.get("busca_doctrina")
    
      mi_lectura = Doctrina.objects.all().order_by('titulo')
      context = {'doctrinas': mi_lectura}
      if busca_doctrina:
                doct=Doctrina.objects.filter(Q(titulo__icontains=busca_doctrina))
                my_lectura = Doctrina.objects.all()
                context = {'doctrinas': doct}
                return render(request, 'rv60app/doctrina.html', context=context)
      return render(request, 'rv60app/doctrina.html', context=context)  
  
  
  
 ########################   Diccionario

def diccionario(request):
        busca_palabra=request.GET.get("busca_palabra")  
    
        mi_lectura = Diccionario.objects.all().order_by('palabra')
        context = {'diccionarios': mi_lectura}
        if busca_palabra:
                ward=Diccionario.objects.filter(Q(palabra__icontains=busca_palabra))
                my_lectura = Diccionario.objects.all()
                context = {'diccionarios': ward}
                return render(request, 'rv60app/diccionario.html', context=context)

        return render(request, 'rv60app/diccionario.html', context=context)   
  
 ########################   Temas

def tema(request):
      busca_tema=request.GET.get("busca_tema")
        
      mi_lectura = Tema.objects.all().order_by('verso_start')
      context = {'temas': mi_lectura}
      if busca_tema:
            tem=Tema.objects.filter(Q(titulo__icontains=busca_tema))
            my_lectura = Tema.objects.all()
            context = {'temas': tem}
            return render(request, 'rv60app/tema.html', context=context)
      return render(request, 'rv60app/tema.html', context=context)    





def porcion(request, start, end, titulo):
#     v = Versiculo.objects.filter(
#         id__range=(start, end)
#     ).select_related('capitulos__libros').annotate(
#         libro_es=F('capitulos__libros__libro_es'),
#         caps_de_libros=F('capitulos__caps_de_libros')
#     )

    v = Versiculo.objects.raw(f""" 
      SELECT * FROM public.rv60app_versiculo 
         inner join public.rv60app_capitulo on rv60app_versiculo.capitulos_id = rv60app_capitulo.id
         inner join public.rv60app_libro on rv60app_capitulo.libros_id = rv60app_libro.id
         where rv60app_versiculo.id between {start} and {end}
		 
""")
    processed_result = []
    last_caps = None  # Track the last processed chapter
    last_libro = None  # Track the last processed book

    for x in v:
        # Reset libro_es only when caps_de_libros changes
        if x.caps_de_libros != last_caps:
            last_caps = x.caps_de_libros
            last_libro = x.libro_es
        else:
            x.caps_de_libros = None  # Clear caps_de_libros for repeated rows
            x.libro_es = None  # Clear libro_es for repeated rows

        processed_result.append(x)

    # Replace None with a blank string for display
    for x in processed_result:
        if x.libro_es is None:
            x.libro_es = ''
        if x.caps_de_libros is None:
            x.caps_de_libros = ''

    contexto = {
        'resultado': processed_result,
        'titulo': titulo,
    }

    return render(request, 'rv60app/tematico.html', contexto)



##################################################################################################

from django.shortcuts import render, get_object_or_404

        
from django.views.generic.detail import DetailView
from .models import Doctrina, Doct_texto, Doct_verso

class DoctrinaDetailView(DetailView):
    model = Doctrina
    template_name = 'doctrina_detail.html'
    context_object_name = 'doctrina'

   

def doctrina_detail_view(request, pk):
    doctrina = get_object_or_404(Doctrina, pk=pk)
    
    doct_textos = Doct_texto.objects.filter(textofk=doctrina).order_by('orden_t')
    doct_versos = Doct_verso.objects.filter(versofk=doctrina).order_by('orden_v')
    

    v2 = []
    for x in doct_versos:
        v = Versiculo.objects.filter(id=(x.verso)
    ).select_related('capitulos__libros').annotate(
        libro_es=F('capitulos__libros__libro_es'),
        caps_de_libros=F('capitulos__caps_de_libros')
    )
    
    
        v2.append(v)
    
        
        context={
            'doct_textos':doct_textos,
            # 'doct_versos':doct_versos,
            'doct_versosx':v2
        }
    return render(request, 'rv60app/doctrina_detail.html', context)
