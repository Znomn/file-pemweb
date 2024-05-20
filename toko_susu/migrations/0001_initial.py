# Generated by Django 5.0.2 on 2024-03-20 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pemasok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pembelian', models.DateTimeField(auto_now_add=True)),
                ('pelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toko_susu.pelanggan')),
            ],
        ),
        migrations.CreateModel(
            name='ProdukSusu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pemasok', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='toko_susu.pemasok')),
            ],
        ),
        migrations.CreateModel(
            name='DetailPembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.PositiveIntegerField()),
                ('pembelian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toko_susu.pembelian')),
                ('produk_susu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toko_susu.produksusu')),
            ],
        ),
    ]
