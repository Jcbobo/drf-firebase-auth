# -*- coding: utf-8 -*-
from django.apps import AppConfig
import os
from django.conf import settings
from .utils import map_firebase_uid_to_username


class CoreConfig(AppConfig):
    name = 'drf_firebase_auth'
    default_auto_field = 'django.db.models.BigAutoField'

