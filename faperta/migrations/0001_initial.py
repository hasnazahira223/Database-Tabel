# Generated by Django 4.1.1 on 2022-10-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosen', models.CharField(max_length=50)),
                ('tendik', models.CharField(max_length=50)),
                ('mahasiswa', models.CharField(max_length=50)),
            ],
        ),
    ]