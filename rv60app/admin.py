from django.contrib import admin
from .models import Libro, Capitulo, Versiculo, Diccionario, Lectura, Tema, Autor, Division, Doctrina, Doct_texto, Doct_verso


# Register your models here.

admin.site.register(Libro)
admin.site.register(Capitulo)
admin.site.register(Versiculo)
admin.site.register(Diccionario)
admin.site.register(Lectura)
admin.site.register(Tema)
admin.site.register(Autor)
admin.site.register(Division)
admin.site.register(Doctrina)
admin.site.register(Doct_texto)
admin.site.register(Doct_verso)