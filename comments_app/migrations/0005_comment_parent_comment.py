# Generated by Django 4.1.7 on 2023-03-11 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0004_remove_comment_parent_comment_delete_childcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments_app.comment'),
        ),
    ]
