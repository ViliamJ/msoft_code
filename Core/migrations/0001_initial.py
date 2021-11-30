# Generated by Django 3.2.8 on 2021-11-30 12:56

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auctioned_item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('type', models.CharField(choices=[('Auctioned/sold', 'Auctioned'), ('Auctioning', 'Auctioning'), ('Scheduled', 'Scheduled')], default='Scheduled', max_length=50)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]