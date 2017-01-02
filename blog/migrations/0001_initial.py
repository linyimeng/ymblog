# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published', models.BooleanField(default=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
            ],
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nickname', models.CharField(null=True, blank=True, max_length=30, unique=True)),
                ('blogname', models.CharField(max_length=30, unique=True)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='blog.BlogUser'),
        ),
    ]
