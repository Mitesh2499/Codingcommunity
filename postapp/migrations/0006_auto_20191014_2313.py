# Generated by Django 2.1.5 on 2019-10-14 17:43

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0005_auto_20191013_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
