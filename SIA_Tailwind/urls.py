from django.urls import path
from . import views

app_name = 'SIA_Tailwind'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('beranda/', views.beranda, name='beranda'),
    path('nilai/', views.nilai, name='nilai'),

    path('presensi/', views.buatPresensi, name='buatPresensi'),
    path('detailKehadiran/', views.cekDetailKehadiran, name='cekDetailKehadiran'),

    path('totalKehadiran/', views.cekTotalKehadiran, name='cekTotalKehadiran'),
]