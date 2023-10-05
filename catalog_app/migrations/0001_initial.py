# Generated by Django 4.2.6 on 2023-10-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('product_title', models.CharField(max_length=200)),
                ('product_unit', models.CharField(max_length=50)),
                ('display_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('description', models.CharField(max_length=250)),
                ('product_pic', models.CharField(blank=True, max_length=200)),
                ('created_by', models.CharField(default='Auto', max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='Auto', max_length=30)),
                ('void', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('password', models.CharField(max_length=250)),
                ('created_by', models.CharField(default='Auto', max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='Auto', max_length=30)),
                ('void', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
    ]
