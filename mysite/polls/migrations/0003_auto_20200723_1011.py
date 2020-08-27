# Generated by Django 3.0.8 on 2020-07-23 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='')),
                ('quntity', models.ImageField(upload_to='')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]