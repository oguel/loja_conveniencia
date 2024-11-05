<<<<<<< HEAD
from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    def post(self, request):
        pass

=======
from django.shortcuts import render
from django.views import View
from .models import *

class Index(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    def post(self, request):
        pass

>>>>>>> c14309da42ebcf068d17d74e5492d1d2180f0b0f
