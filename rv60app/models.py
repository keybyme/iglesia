
from django.db import models

#########################################################

class Autor(models.Model):
    profeta = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profeta}"

#########################################################    
    
class Division(models.Model):
    grupo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.grupo}"    

#########################################################

class Libro(models.Model):
    link = models.CharField(max_length=150, blank=True, null=True)
    libro_en = models.CharField(max_length=100, blank=True, null=True)
    libro_es = models.CharField(max_length=100, blank=True, null=True)
    temaprincipal = models.CharField(max_length=500, blank=True, null=True)
    textos = models.CharField(max_length=500, blank=True, null=True)
    year = models.CharField(max_length=15, blank=True, null=True)
    author = models.ForeignKey(Autor, models.DO_NOTHING, blank=True, null=True)
    divisiones = models.ForeignKey(Division, models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return f"{self.link} | {self.libro_en} | {self.libro_es} | {self.temaprincipal} | {self.textos} | {self.year} | {self.author} | {self.divisiones}"    

#########################################################
    
class Capitulo(models.Model):
    caps_de_libros = models.IntegerField(blank=True, null=True)
    libros = models.ForeignKey('Libro', models.DO_NOTHING)    
    
    def __str__(self):
        return f"{self.caps_de_libros} | {self.libros}"    

#########################################################

class Versiculo(models.Model):
    contenido = models.TextField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    capitulos = models.ForeignKey(Capitulo, models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return f"{self.contenido} | {self.numero} | {self.content} | {self.capitulos}"    
    
#########################################################
       
class Tema(models.Model):
    titulo = models.TextField()
    verso_start = models.IntegerField()
    verso_end = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} | {self.verso_start} | {self.verso_end}"

#########################################################

class Diccionario(models.Model):
    palabra = models.CharField(max_length=100, blank=True, null=True)
    definicion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.palabra} | {self.definicion}"

#########################################################

class Lectura(models.Model):
    mes = models.IntegerField()
    dia = models.IntegerField()
    st_am = models.IntegerField()
    end_am = models.IntegerField()
    st_pm = models.IntegerField()
    end_pm = models.IntegerField()

    def __str__(self):
        return f"{self.mes} | {self.dia} | {self.st_am} | {self.end_am} | {self.st_pm} | {self.end_pm}"

#########################################################

class Doctrina(models.Model):
    titulo = models.CharField(max_length=150, blank=True)
    maintexto = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.titulo} | {self.maintexto}"    

#########################################################

class Doct_texto(models.Model):
    texto = models.TextField(blank=True, null=True)
    orden_t = models.IntegerField(blank=True, null=True)
    textofk = models.ForeignKey(Doctrina, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.textofk.titulo} | {self.orden_t} | {self.texto}"
    
#########################################################

class Doct_verso(models.Model):
    verso = models.IntegerField(blank=True, null=True)
    orden_v = models.IntegerField(blank=True, null=True)
    # versfk = models.ForeignKey(Versiculo, models.DO_NOTHING, blank=True, null=True)
    versofk = models.ForeignKey(Doctrina, models.DO_NOTHING, blank=True, null=True)
 
    def __str__(self):
        return f"{self.versofk.titulo} | {self.orden_v} | {self.verso}"
    
#########################################################

