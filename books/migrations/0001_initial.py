# Generated by Django 4.2.2 on 2023-07-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('book_genre', models.CharField(max_length=50)),
                ('synopsis', models.CharField(max_length=200)),
                ('publishing_company', models.CharField(max_length=50)),
                ('num_copies', models.IntegerField()),
            ],
        ),
    ]
