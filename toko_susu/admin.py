from django.contrib import admin
from .models import Pemasok, ProdukSusu, Pelanggan, Pembelian, DetailPembelian

# Register your models here.

admin.site.register(Pemasok)
class PemasokAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat']
    search_fields = ['nama']

admin.site.register(ProdukSusu)
class ProdukSusuAdmin(admin.ModelAdmin):
    list_display = ['nama', 'harga', 'pemasok']
    search_fields = ['nama']

admin.site.register(Pelanggan)
class PelangganAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat']
    search_fields = ['nama']

admin.site.register(Pembelian)
class PembelianAdmin(admin.ModelAdmin):
    list_display = ['pelanggan', 'tanggal_pembelian']
    search_fields = ['pelanggan']

admin.site.register(DetailPembelian)
class DetailPembelianAdmin(admin.ModelAdmin):
    list_display = ['produk_susu', 'jumlah', 'pembelian']
    search_fields = ['produk_susu']