#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from fastkml import kml

from base.models import City, State
from quilombola.models import Community, Phase


class Command(BaseCommand):
    help = 'Import All KML Bases into app'

    def load_comunidades_kilombolas(self):
        
        my_kml = kml.KML()

        with open('latentes_data/Latentes - Comunidades quilombolas.kml', 'rb') as kml_file:
            my_kml.from_string(kml_file.read())

        list_descricao = []
        for document in my_kml.features():
            for index, item in enumerate(document.features()):
                extra_data_dict = {}
                extra_data = item.extended_data
                for element in extra_data.elements:
                    extra_data_dict.update({element.name: element.value})

                #print(extra_data_dict); break
                if extra_data_dict.get('uf_sigla'):
                    state, created = State.objects.get_or_create(initials=extra_data_dict['uf_sigla'])
                else:
                    state = None

                if extra_data_dict.get('municipio'):
                    city, created = City.objects.get_or_create(
                        name=str(extra_data_dict['municipio']).lower().capitalize(), 
                        state=state)
                else:
                    city = None

                new_phase, created = Phase.objects.get_or_create(
                    name=extra_data_dict['fase'],
                    description=extra_data_dict['descrição']
                )

                new_community = Community()
                new_community.name = str(extra_data_dict.get('nome', 'Sem nome')).lower().capitalize()
                new_community.family_no = int(extra_data_dict['familias']) if extra_data_dict.get('familias') else None
                new_community.city = city
                new_community.phase = new_phase 
                area = extra_data_dict['area'] if extra_data_dict.get('area') else None
                new_community.area = area

                polygon = GEOSGeometry(str(item.geometry))
                if polygon.geom_type == 'Polygon':
                    new_community.geometry = polygon
                    new_community.save()
                    print(f'# Processed {new_community}')
                else:
                    print(f'# ERROR IMPORTING {new_community} - GEOM {polygon.geom_type}')

                new_community.save()


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Importing Comunidade Quilombolas'))
        self.load_comunidades_kilombolas()
        self.stdout.write(self.style.SUCCESS('Done'))
