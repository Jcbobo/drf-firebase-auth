# -*- coding: utf-8 -*-
from django.apps import AppConfig
import os
from django.conf import settings
from .utils import map_firebase_uid_to_username


class CoreConfig(AppConfig):
    name = 'drf_firebase_auth'
    default_auto_field = 'django.db.models.BigAutoField'

    SER_SETTINGS = getattr(settings, 'DRF_FIREBASE_AUTH', None)
    # allow anonymous requests without Authorization header set
    ALLOW_ANONYMOUS_REQUESTS = getattr(settings, 'ALLOW_ANONYMOUS_REQUESTS', False)
    # path to JSON file with firebase secrets
    FIREBASE_SERVICE_ACCOUNT_KEY = getattr(settings, 'FIREBASE_SERVICE_ACCOUNT_KEY', '')
    # allow creation of new local user in db
    FIREBASE_CREATE_LOCAL_USER = getattr(settings, 'FIREBASE_CREATE_LOCAL_USER', True)
    # attempt to split firebase user.display_name and set local user
    # first_name and last_name
    FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME = getattr(settings, 'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME', True)
    # commonly JWT or Bearer (e.g. JWT <token>)
    FIREBASE_AUTH_HEADER_PREFIX = getattr(settings, 'FIREBASE_AUTH_HEADER_PREFIX', 'JWT')
    # verify that JWT has not been revoked
    FIREBASE_CHECK_JWT_REVOKED = getattr(settings, 'FIREBASE_CHECK_JWT_REVOKED', True)
    # require that firebase user.email_verified is True
    FIREBASE_AUTH_EMAIL_VERIFICATION = getattr(settings, 'FIREBASE_AUTH_EMAIL_VERIFICATION', False)
    # function should accept firebase_admin.auth.UserRecord as argument
    # and return str
    FIREBASE_USERNAME_MAPPING_FUNC = 'drf_firebase_auth.utils.map_firebase_uid_to_username'
