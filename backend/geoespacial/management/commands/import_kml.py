#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import KML Bases into app'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str)

    def handle(self, *args, **options):
        for kml_file in options['files']:
            try:
                self.stdout.write(self.style.SUCCESS(f'OPENING FILE {kml_file}'))
            except Poll.DoesNotExist:
                raise CommandError('File does not exists')

            self.stdout.write(self.style.SUCCESS('Done'))
