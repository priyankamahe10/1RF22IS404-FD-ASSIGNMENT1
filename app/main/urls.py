from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
   path('hello/',views.hello,name='hello'),
   path('fact/',views.fact,name="fact"),
   path('index/',views.index,name='index'),
   path('mode/',views.mode,name="mode"),
   path('icic/',views.icic,name='icic'),
   path('hol/',views.hol,name="hol"),
]