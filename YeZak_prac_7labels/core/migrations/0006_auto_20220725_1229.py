# Generated by Django 3.2.14 on 2022-07-25 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('interior_id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'interior',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_pic', models.ImageField(upload_to='uploads')),
                ('price', models.IntegerField()),
                ('item_size_width', models.CharField(max_length=45)),
                ('item_size_height', models.CharField(max_length=45)),
                ('details', models.TextField(blank=True, max_length=2000, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('item_name', models.CharField(blank=True, max_length=45, null=True)),
                ('tag_list', models.TextField(blank=True, null=True)),
                ('prediction', models.CharField(choices=[('orientalism', 'orientalism'), ('realism', 'realism'), ('animation', 'animation'), ('pencil', 'pencil'), ('impressionism', 'impressionism'), ('abstract', 'abstract'), ('popart', 'popart')], max_length=22)),
            ],
            options={
                'db_table': 'item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
                ('profile_pic', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(max_length=45)),
                ('phone_number', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('msg_id', models.IntegerField(db_column='msg_ID', primary_key=True, serialize=False)),
                ('msg_content', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.item')),
                ('state', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'deals',
                'managed': False,
            },
        ),
    ]
