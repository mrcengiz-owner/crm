# Generated by Django 4.1.7 on 2023-04-12 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('isim', models.CharField(max_length=150)),
                ('soyisim', models.CharField(max_length=150)),
                ('adres', models.CharField(max_length=150)),
                ('il', models.CharField(max_length=150)),
                ('ilce', models.CharField(max_length=150)),
                ('postakod', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=150)),
                ('telefon', models.CharField(max_length=15)),
            ],
        ),
    ]
