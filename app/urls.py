from django.urls import path

from . import views

app_name='something'
urlpatterns=[
    path('First/',views.Cond),
    path('second/',views.Loop),
]