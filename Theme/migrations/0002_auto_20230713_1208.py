# Generated by Django 3.2.19 on 2023-07-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_image', models.ImageField(blank=True, null=True, upload_to='client')),
                ('client_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_alttag', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(blank=True, default='', null=True)),
                ('name', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='admin@gmail.com', max_length=254, null=True)),
                ('connect_date', models.DateField(auto_now_add=True, null=True)),
                ('connect_time', models.TimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, default=0, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_image', models.ImageField(blank=True, null=True, upload_to='testimonial')),
                ('testimonial_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('testimonial_position', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('testimonial_discription', models.TextField(blank=True, default='', null=True)),
                ('testimonial_status', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('testimonial_tag', models.CharField(blank=True, default=0, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='time',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='template_time',
        ),
    ]