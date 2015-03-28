from django.contrib import admin
from models import Articulo, Autor
# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('titulo','autor','created') # Que campos se van a listar en el admin

#Se agregan los modelos al admin
admin.site.register(Articulo, ArticuloAdmin) 
admin.site.register(Autor)