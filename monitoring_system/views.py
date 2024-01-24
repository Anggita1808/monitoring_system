from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    Tampilan (view) untuk halaman utama atau indeks.
    """
    return HttpResponse("Selamat datang di aplikasi Django Anda!")
