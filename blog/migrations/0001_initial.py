# Generated by Django 2.0.9 on 2018-10-28 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('linea', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cliente'),
        ),
        migrations.AddField(
            model_name='carro',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Servicio'),
        ),
    ]