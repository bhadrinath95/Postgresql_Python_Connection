# Generated by Django 2.2.7 on 2020-02-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
    ]