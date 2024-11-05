<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
=======
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
>>>>>>> c14309da42ebcf068d17d74e5492d1d2180f0b0f
]