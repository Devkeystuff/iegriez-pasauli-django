# Generated by Django 3.2.3 on 2021-06-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_rename_question_mapquestion_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapquestion',
            name='answer_message',
        ),
        migrations.AddField(
            model_name='mapanswer',
            name='answer_message',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
