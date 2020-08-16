from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('',home,name="home"),#
    path('contact/',contact,name="contact"),#
    path('gallery/',gallery,name="gallery"),#
    path('result/',result,name="result"),#
    path('admission/',admission,name="admission"),#
    path('history/',history,name="history"),
    path('school_family/',school_family,name="school_family"),
    path('memories/',memories,name="memories"),
    path('co_curricular/',co_curricular,name="co_curricular"),
]  