# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationprofile',
            name='user',
            field=models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
