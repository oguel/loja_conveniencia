<<<<<<< HEAD
from django.contrib import admin

from .models import *

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome']
    search_fields = ['nome']
    inlines = [ProdutoInline,]
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','nome','fabricante','preco','categoria']
    search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
=======
from django.contrib import admin

from .models import *

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nome']
    search_fields = ['nome']
    inlines = [ProdutoInline,]
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','nome','fabricante','preco','categoria']
    search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
>>>>>>> c14309da42ebcf068d17d74e5492d1d2180f0b0f
admin.site.register(Produto, ProdutoAdmin)