# Generated by Django 3.1.4 on 2021-04-03 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150, verbose_name="Nom de l'adhérent ")),
                ('prenom', models.CharField(max_length=150, verbose_name="Prénom de l'adhérent")),
                ('telephone', models.CharField(max_length=150, verbose_name="Téléphone de l'adhérent")),
                ('email', models.EmailField(max_length=254, verbose_name="Email de l'adhérent")),
            ],
        ),
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150, verbose_name="Nom de l'auteur ")),
                ('prenom', models.CharField(max_length=150, verbose_name="Prénom de l'auteur")),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150, verbose_name='Titre de la categorie ')),
                ('description', models.TextField(max_length=150, verbose_name='Description de la catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=150, verbose_name='Titre du livre ')),
                ('editeur', models.CharField(max_length=150, verbose_name='Editeur du livre ')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_auteur', to='bibliotheque.auteur')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_categorie', to='bibliotheque.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Bibliotheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRetour', models.DateField()),
                ('datePris', models.DateField(auto_now_add=True)),
                ('adherent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_adherent', to='bibliotheque.adherent')),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_livre', to='bibliotheque.livre')),
            ],
        ),
    ]
