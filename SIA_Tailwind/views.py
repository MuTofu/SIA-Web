from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
    return render(request, "LoginPage.html")

def beranda(request):
    return render(request, "BerandaGuruPage.html")

def nilai(request):
    return render(request, "NilaiGuruPage.html")

def buatPresensi(requests):
    return render(requests, "BuatPresensiGuruPage.html")

def cekDetailKehadiran(requests):
    return render(requests, "KehadiranGuruPage.html")

def cekTotalKehadiran(requests):
    return render(requests, "TotalKehadiranGuruPage.html")

def inputDataSiswa(requests):
    return render(requests, "InputDataSiswaAdmin.html")

def inputDataGuru(requests):
    return render(requests, "InputDataGuruAdmin.html")

def inputDataMapel(request):
    return render(request, "InputDataMapelAdmin.html")

def dataSiswa(requests):
    return render(requests, "DataSiswaAdmin.html")

def dataGuru(requests):
    return render(requests, "DataGuruAdmin.html")

def dataMapel(requests):
    return render(requests, "DataMapelAdmin.html")