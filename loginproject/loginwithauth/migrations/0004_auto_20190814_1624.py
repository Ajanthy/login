# Generated by Django 2.2.3 on 2019-08-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginwithauth', '0003_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('geo_tag', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'complaints',
            },
        ),
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
