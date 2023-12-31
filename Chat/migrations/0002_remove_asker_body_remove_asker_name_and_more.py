# Generated by Django 4.1.2 on 2023-02-27 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asker',
            name='body',
        ),
        migrations.RemoveField(
            model_name='asker',
            name='name',
        ),
        migrations.RemoveField(
            model_name='botai',
            name='BotAns',
        ),
        migrations.RemoveField(
            model_name='botai',
            name='name',
        ),
        migrations.CreateModel(
            name='Botbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BotAns', models.TextField(blank=True, max_length=1000, null=True)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.botai')),
            ],
        ),
        migrations.CreateModel(
            name='Askerbody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=1000, null=True)),
                ('asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chat.asker')),
            ],
        ),
    ]
