# Generated by Django 4.0.3 on 2022-03-18 10:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_alter_user_face_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_face',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
