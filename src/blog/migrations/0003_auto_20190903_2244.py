# Generated by Django 2.2 on 2019-09-03 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogposts_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPosts',
            new_name='BlogPost',
        ),
    ]