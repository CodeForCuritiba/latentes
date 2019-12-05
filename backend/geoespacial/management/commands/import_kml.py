#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from fastkml import kml


class Command(BaseCommand):
    help = 'Import KML Bases into app'

    def load_comunidades_kilombolas(self):
        
        my_kml = kml.KML()

        with open('latentes_data/Latentes - Comunidades quilombolas.kml', 'rb') as kml_file:
            my_kml.from_string(kml_file.read())

        list_descricao = []
        for feature in my_kml.features():
            for feat in feature.features():
                extra_data_dict = {}
                extra_data = feat.extended_data
                for element in extra_data.elements:
                    extra_data_dict.update({element.name: element.value})

                print(extra_data_dict)
                #feat.geometry

                #import ipdb; ipdb.set_trace()
                break
                

    def handle(self, *args, **options):
        self.load_comunidades_kilombolas()

        self.stdout.write(self.style.SUCCESS('Done'))
