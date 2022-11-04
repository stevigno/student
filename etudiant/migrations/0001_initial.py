# Generated by Django 4.1.2 on 2022-11-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('prenons', models.CharField(max_length=100)),
                ('niveau', models.CharField(max_length=50)),
                ('filiere', models.CharField(max_length=50)),
                ('matricule', models.CharField(max_length=32, unique=True)),
                ('adresse', models.CharField(blank=True, max_length=200)),
                ('actifs', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]