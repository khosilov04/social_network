# Generated by Django 5.0.3 on 2024-03-20 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_commentpost_like_count_post_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cover_image',
            field=models.ImageField(default='user/setting/timeline.avif', upload_to='user/setting'),
        ),
    ]
