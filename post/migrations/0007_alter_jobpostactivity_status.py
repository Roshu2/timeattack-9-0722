# Generated by Django 4.0.6 on 2022-07-22 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_status'),
        ('post', '0006_jobpostactivity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostactivity',
            name='status',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.status'),
        ),
    ]
