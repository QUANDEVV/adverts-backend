# Generated by Django 4.2.6 on 2024-06-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_image', models.ImageField(upload_to='avatars')),
                ('ig_link', models.URLField(max_length=255)),
                ('onlyfans_link', models.URLField(max_length=255)),
                ('likes', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
                ('is_booked', models.BooleanField(default=False)),
                ('booked_at', models.DateTimeField(blank=True, null=True)),
                ('booking_start', models.DateTimeField(blank=True, null=True)),
                ('booking_end', models.DateTimeField(blank=True, null=True)),
                ('slot_number', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='girl',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='video',
            name='girl',
        ),
        migrations.DeleteModel(
            name='Girls',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
