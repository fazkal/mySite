# Generated by Django 4.2.14 on 2024-09-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_options_rename_subjcet_comment_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
