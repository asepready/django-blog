#!/usr/bin/env python
# encoding: utf-8

from django.core.management.base import BaseCommand
from oauth.models import OAuthUser
from core.utils import save_user_avatar


class Command(BaseCommand):
    help = 'sync user avatar'

    def handle(self, *args, **options):
        users = OAuthUser.objects.filter(picture__isnull=False).exclude(
            picture__istartswith='https://').all()
        self.stdout.write('Start syncing {count} User avatars'.format(count=len(users)))
        for u in users:
            self.stdout.write('Start syncing:{id}'.format(id=u.nikename))
            url = u.picture
            url = save_user_avatar(url)
            if url:
                self.stdout.write(
                    'End sync:{id}.url:{url}'.format(
                        id=u.nikename, url=url))
                u.picture = url
                u.save()
        self.stdout.write('End sync')
