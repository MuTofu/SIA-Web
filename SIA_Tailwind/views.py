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