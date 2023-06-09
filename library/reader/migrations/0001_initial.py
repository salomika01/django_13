# Generated by Django 4.2.2 on 2023-06-09 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('favorite_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.book')),
            ],
        ),
    ]