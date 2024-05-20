from django.db import models

class Pemasok(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Pemasok"

class ProdukSusu(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    pemasok = models.OneToOneField(Pemasok, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "2. Produk Susu"

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "3. Pelanggan"

class Pembelian(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    tanggal_pembelian = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pelanggan
    
    class Meta:
        verbose_name_plural = "4. Pembelian"

class DetailPembelian(models.Model):
    pembelian = models.ForeignKey(Pembelian, on_delete=models.CASCADE)
    produk_susu = models.ForeignKey(ProdukSusu, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produk_susu.nama} dalam pembelian {self.pembelian}"
    
    class Meta:
        verbose_name_plural = "5. Detail Pembelian"

### Penjelasan ###
'''
1. One to One = terdapat pada pemasok dan produk susu, jadi pemasok hanya menyediakan satu produk susu,
contoh pemasok 1 hanya menyediakan susu sapi untuk ke produk susu.
2. One to Many = terdapat pada pelanggan dan pembelian, jadi contohnya pada satu pembelian bisa terdapat banyak produk susu,
tetapi dalam setiap pembelian hanya terkait dengan 1 pelanggan.
3. Many to Many = terdapat pada Detail Pembelian, jadi setiap pembelian dapat terdiri dari banyak produk susu,
dan setiap produk susu dapat terjual dalam banyak pembelian,
ini relasi many to many yang ada di antara model Produk susu dan Pembelian yang diterapkan lewat Detail Pembelian
'''