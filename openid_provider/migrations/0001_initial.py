# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(unique=True, max_length=200, blank=True)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['openid'],
                'verbose_name': 'OpenID',
                'verbose_name_plural': 'OpenIDs',
            },
        ),
        migrations.CreateModel(
            name='TrustedRoot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trust_root', models.CharField(max_length=200)),
                ('openid', models.ForeignKey(to='openid_provider.OpenID')),
            ],
        ),
    ]
