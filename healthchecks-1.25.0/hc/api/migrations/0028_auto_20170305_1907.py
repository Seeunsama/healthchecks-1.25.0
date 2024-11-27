# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [("api", "0027_auto_20161213_1059")]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="code",
            field=models.UUIDField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "OpsGenie"),
                    ("victorops", "VictorOps"),
                    ("discord", "Discord"),
                ],
                max_length=20,
            ),
        ),
    ]
