# Generated by Django 4.1.3 on 2023-08-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0006_alter_subject_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='event_img/')),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='subject_logos/'),
        ),
    ]
