# Generated by Django 4.0.3 on 2022-03-18 09:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_user_face_age_user_face_gender_user_face_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_face',
            name='account_number',
        ),
        migrations.AlterField(
            model_name='user_face',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
