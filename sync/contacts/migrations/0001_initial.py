# Generated by Django 2.2.7 on 2019-11-16 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=256)),
                ('last_name', models.CharField(blank=True, default='', max_length=256)),
                ('company', models.CharField(blank=True, default='', max_length=256)),
                ('title', models.CharField(blank=True, default='', max_length=256)),
                ('notes', models.TextField(blank=True, default='')),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(1, 'Mobile'), (2, 'Work'), (3, 'Home'), (4, 'Other')])),
                ('name_if_other', models.CharField(blank=True, default='', max_length=128)),
                ('value', models.CharField(max_length=32)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
            ],
        ),
    ]
