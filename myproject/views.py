from urllib import request
from django.shortcuts import render
from berita.models import Artikel, Kategori

def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori == None:
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        print("Bukan ALL")
        get_kategori = Kategori.objects.filter(nama=kategori)
        if get_kategori.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=get_kategori[0])
            menu_aktif = kategori
        else:
            menu_aktif = "ALL"
            data_artikel = []


    data_kategori = Kategori.objects.all()
    context = {
        'title':'Selamat Datang',
        'data_artikel': data_artikel,
        'data_kategori': data_kategori,
        'menu_aktif': menu_aktif
    }
    return render(request, template_name, context)

def about (request):
    template_name = "halaman/about.html"
    context ={
        'title':'selamat datang di halaman about',
        'umur': 20,
    }
    return render(request, template_name, context)

def contact (request):
    template_name = "halaman/contact.html"
    context ={
        'title':'selamat datang di halaman about',
        'umur': 20,
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name = 'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(slug=slug)
    print(artikel.author)
    context = {
        'title': artikel.judul,
        'artikel': artikel
    }
    return render(request, template_name, context)