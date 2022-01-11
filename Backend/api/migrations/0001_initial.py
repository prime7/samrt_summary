# Generated by Django 3.2.5 on 2021-07-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_link', models.URLField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('summary', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], default=0, null=True)),
            ],
        ),
    ]