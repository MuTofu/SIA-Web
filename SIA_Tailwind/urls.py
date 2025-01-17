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

    path('inputdatasiswa/', views.inputDataSiswa, name='inputdatasiswa'),

    path('inputdataguru/', views.inputDataGuru, name='inputdataguru'),

    path('inputdatamapel/', views.inputDataMapel, name='inputdatamapel'),

    path('datasiswa/', views.dataSiswa, name='datasiswa'),

    path('dataguru/', views.dataGuru, name='dataguru'),

    path('datamapel/', views.dataMapel, name='datamapel'),

]