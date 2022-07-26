# Generated by Django 3.2.14 on 2022-07-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag_list',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='prediction',
            field=models.CharField(choices=[('theme1', 'theme1'), ('theme2', 'theme2'), ('theme3', 'theme3'), ('theme4', 'theme4'), ('theme5', 'theme5')], max_length=22),
        ),
    ]