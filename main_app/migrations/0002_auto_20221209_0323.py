# Generated by Django 3.2.5 on 2022-12-09 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['number']},
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=250)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.test')),
            ],
        ),
    ]
