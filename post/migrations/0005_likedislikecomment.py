# Generated by Django 3.2 on 2022-09-15 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_likedisliketweet_tweetstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.tweetstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'comment')},
            },
        ),
    ]
