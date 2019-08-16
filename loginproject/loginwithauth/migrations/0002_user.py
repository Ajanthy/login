# Generated by Django 2.2.3 on 2019-08-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginwithauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nic', models.CharField(max_length=12)),
                ('nickname', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phoneNo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]